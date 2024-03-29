from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Spark Test App").getOrCreate()

# Read some data (modify path as needed)
data = spark.read.text("/path/to/data.txt")

# Do some basic transformations (count number of lines)
num_lines = data.count()

# Print the results
print(f"Number of lines: {num_lines}")

# Stop the SparkSession
spark.stop()
