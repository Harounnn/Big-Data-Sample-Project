from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("MusicDataAnalysis") \
    .getOrCreate()

data_path = "file:///opt/bitnami/spark/data.csv"
df = spark.read.csv(data_path, header=True)

df.show(5)

df.describe().show()


num_artists = df.select("artist").distinct().count()
print("Number of unique artists:", num_artists)

most_popular_chart = df.groupBy("chart") \
    .count() \
    .orderBy("count", descending=True) \
    .head(1) \
    ["chart"] \
    .first()
print("Most popular chart:", most_popular_chart)


df_with_date = df.withColumn("date", df["date"].cast("date"))
df_by_date = df_with_date.groupBy("date") \
    .agg(
        {"artist": "count"}).orderBy("date")

spark.stop()
