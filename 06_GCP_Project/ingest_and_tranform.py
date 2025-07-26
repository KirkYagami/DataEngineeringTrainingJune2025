import requests
import os
from datetime import datetime
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from utils.helper import download_data, BQ_SCHEMA
from google.cloud.exceptions import NotFound


# TASK: Implement logging -> logging module, logger.info(), ..., write the logs a .log file

from dotenv import load_dotenv

load_dotenv()


GITHUB_RAW_CSV_URL = os.getenv("GITHUB_RAW_CSV_URL")
LOCAL_RAW_DATA_DIR = os.getenv("LOCAL_RAW_DATA_DIR")
LOCAL_CLEANED_DATA_DIR = os.getenv("LOCAL_CLEANED_DATA_DIR")
FILE_PREFIX = os.getenv("FILE_PREFIX")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BQ_DATASET_NAME = os.getenv("BQ_DATASET_NAME")
BQ_TABLE_NAME = os.getenv("BQ_TABLE_NAME")



def clean_data_with_pandas(raw_filepath, cleaned_dir, file_prefix):
    if not os.path.exists(cleaned_dir):
        os.makedirs(cleaned_dir)

    if raw_filepath is None:
        print("No raw file to clean. Skipping cleaning step.")
        return None
    
    print(f"Cleaning data from: {raw_filepath}")
    try:
        df = pd.read_csv(raw_filepath)

        df['released_date'] = pd.to_datetime(df['released_at'], format="%d %b %Y", errors='coerce')

        df['added_date'] = pd.to_datetime(df['added_at'], format="%B %d, %Y", errors='coerce')

        df['runtime_minutes'] = df['runtime'].astype(str).str.replace(' min', '', regex=False)

        df['runtime_minutes'] = pd.to_numeric(df['runtime_minutes'], errors='coerce').astype('Int64')

        df['metascore_int'] = pd.to_numeric(df['metascore'], errors='coerce').astype('Int64')

        df['imdb_rating_float'] = pd.to_numeric(df['imdb_rating'], errors='coerce').astype(float)

        df['imdb_votes_int'] = df['imdb_votes'].astype(str).str.replace(',', '', regex=False)
        df['imdb_votes_int'] = pd.to_numeric(df['imdb_votes_int'], errors='coerce').astype('Int64')   


        columns_to_drop = ["released_at", "added_at", "runtime", "metascore", "imdb_rating", "imdb_votes"]
        df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

        critical_columns = [
            'imdb_id',           
            'title',
            'type',
            'year',
            'genre'
            ]

        df.dropna(subset=critical_columns, inplace=True)


        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        cleaned_filename = f"{file_prefix}_cleaned_{timestamp}.csv"

        cleaned_filepath = os.path.join(cleaned_dir, cleaned_filename)

        df.to_csv(cleaned_filepath, index=False)


        print(f"Cleaned data saved locally to: {cleaned_filepath}")
        print("\nSchema after cleaning and casting with Pandas:")
        df.info()
        print("\nFirst row of cleaned data:")
        print(df.head(1).to_string())

        return cleaned_filepath
    
    except Exception as e:
        print(f"Error during data cleaning with Pandas: {e}")
        return None
    

def upload_to_gcs(bucket_name, source_filepath, destination_blob_name, project_id):
    if source_filepath is None:
        print("No file to upload to GCS. Skipping GCS upload step.")
        return None
    
    storage_client = storage.Client(project=project_id)
    bucket = storage_client.bucket(bucket_name)

    try:
        bucket.reload()
        print(f"Bucket '{bucket_name}' already exists.")
    except NotFound:
        print(f"Bucket '{bucket_name}' does not exist. Creating it...")
        bucket.create(location='US-CENTRAL1') 
        print(f"Bucket '{bucket_name}' created.")

    blob = bucket.blob(destination_blob_name)

    print(f"Uploading {source_filepath} to gs://{bucket_name}/{destination_blob_name}")

    try:
        blob.upload_from_filename(source_filepath)
        print(f"File uploaded to GCS: gs://{bucket_name}/{destination_blob_name}")
        return f"gs://{bucket_name}/{destination_blob_name}"
    except Exception as e:
        print(f"Error uploading file to GCS: {e}")
        return None
    


def load_gcs_to_bigquery(gcs_uri, dataset_id, table_id, project_id, schema):
    if gcs_uri is None:
        print("No GCS URI to load to BigQuery. Skipping BigQuery load step.")
        return   

    bigquery_client = bigquery.Client(project=project_id)
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    try:
        bigquery_client.get_dataset(dataset_ref)
        print(f"Dataset '{dataset_id}' already exists.")
    except NotFound:
        print(f"Dataset '{dataset_id}' does not exist. Creating it...")
        dataset = bigquery.Dataset(dataset_ref)
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US-CENTRAL1" # same as gcs bucket region
        bigquery_client.create_dataset(dataset, timeout=30)
        print(f"Dataset '{dataset_id}' created.")

    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=False,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )


    print(f"Loading data from {gcs_uri} to {dataset_id}.{table_id}")
    try:
        load_job = bigquery_client.load_table_from_uri(
            gcs_uri, table_ref, job_config=job_config
        )

        load_job.result() 
        print(f"Load job completed. Rows loaded: {load_job.output_rows}")
    except Exception as e:
        print(f"Error loading data to BigQuery: {e}")



if __name__ == "__main__":
    raw_downloaded_file_path = download_data(GITHUB_RAW_CSV_URL, LOCAL_RAW_DATA_DIR, FILE_PREFIX)

    cleaned_file_path = clean_data_with_pandas(raw_downloaded_file_path, LOCAL_CLEANED_DATA_DIR, FILE_PREFIX)

    if cleaned_file_path:
        gcs_blob_name = os.path.basename(cleaned_file_path)
        gcs_uri = upload_to_gcs(GCS_BUCKET_NAME, cleaned_file_path, gcs_blob_name, GCP_PROJECT_ID)
    else:
        gcs_uri = None
        print("Skipping GCS upload due to no cleaned file.")


    load_gcs_to_bigquery(gcs_uri, BQ_DATASET_NAME, BQ_TABLE_NAME, GCP_PROJECT_ID, BQ_SCHEMA)



    print("\nEnd of script. Data pipeline execution attempt complete.")
