from pyspark.sql import SparkSession


from pyspark.sql.functions import input_file_name, when, lit

# Create Spark session
spark = SparkSession.builder \
                    .appName("Healthcare CPT_Codes Ingestion") \
                    .getOrCreate()


               
           
BUCKET_NAME = "healthcare-bucket-28-07-2025"       
CPT_CODES_BUCKET_PATH = f"gs://{BUCKET_NAME}/landing/cptcodes/*.csv"
BQ_TABLE = "active-district-466711-i0.bronze_dataset.cptcodes"
TEMP_GCS_BUCKET = f"{BUCKET_NAME}/temp/"
                    
                    
cpt_df = spark.read.csv(CPT_CODES_BUCKET_PATH, header=True)

for col in cptcodes_df.columns:
    new_col = col.replace(" ", "_").lower()
    cptcodes_df = cptcodes_df.withColumnRenamed(col, new_col)

    

cptcodes_df.columns

# write to bigquery
(cptcodes_df.write
            .format("bigquery")
            .option("table", BQ_TABLE)
            .option("temporaryGcsBucket", TEMP_GCS_BUCKET)
            .mode("overwrite")
            .save())