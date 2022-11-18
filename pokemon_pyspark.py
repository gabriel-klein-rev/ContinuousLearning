from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local") \
    .appName("pokemon") \
    .getOrCreate()
sc = spark.sparkContext()

pokemon_df = spark.read \
    .option("header", True) \
    .option("InferSchema", True) \
    .csv("s3a://continuouslearning/pokemon.csv")

pokemon_df.createOrReplaceTempView("pokemon")
avgAttackDF = spark.sql("SELECT Generation, AVG(Attack) as `Average Attack` FROM pokemon GROUP BY Generation ORDER BY Generation")
avgAttackDF.show()

spark.close()