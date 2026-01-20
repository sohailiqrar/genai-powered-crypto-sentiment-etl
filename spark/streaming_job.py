from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

spark = SparkSession.builder.appName("crypto-sentiment-stream").getOrCreate()

event_hub_conf = {
    'eventhubs.connectionString': dbutils.secrets.get(
        scope="eventhub-scope", 
        key="eventhub-connection")
    }

raw_df = (
    spark.readStream
         .format("eventhubs")
         .options(**event_hub_conf)
         .load()
)

