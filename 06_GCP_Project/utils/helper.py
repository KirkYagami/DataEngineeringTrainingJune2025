import os
from datetime import datetime 
import requests
from google.cloud import bigquery


def download_data(url, local_dir, file_prefix):
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local_filename = f"{file_prefix}_raw_{timestamp}.csv"
    local_filepath = os.path.join(local_dir, local_filename)

    print(f"Downloading data from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(local_filepath, "wb") as file:
            file.write(response.content)
        print(f"Successfully downloaded raw file to: {local_filepath}")
        return local_filepath
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file from {url}. Error: {e}")
        return None





BQ_SCHEMA = [
    bigquery.SchemaField("imdb_id", "STRING"),
    bigquery.SchemaField("title", "STRING"),
    bigquery.SchemaField("plot", "STRING"),
    bigquery.SchemaField("type", "STRING"),
    bigquery.SchemaField("rated", "STRING"),
    bigquery.SchemaField("year", "STRING"),
    bigquery.SchemaField("genre", "STRING"),
    bigquery.SchemaField("director", "STRING"),
    bigquery.SchemaField("writer", "STRING"),
    bigquery.SchemaField("actors", "STRING"),
    bigquery.SchemaField("language", "STRING"),
    bigquery.SchemaField("country", "STRING"),
    bigquery.SchemaField("awards", "STRING"),
    bigquery.SchemaField("released_date", "DATE"),
    bigquery.SchemaField("added_date", "DATE"),
    bigquery.SchemaField("runtime_minutes", "INTEGER"),
    bigquery.SchemaField("metascore_int", "INTEGER"),
    bigquery.SchemaField("imdb_rating_float", "FLOAT"),
    bigquery.SchemaField("imdb_votes_int", "INTEGER"),
]




print('Helper module is getting imported')

if __name__ == "__main__":
    pass

