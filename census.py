import re
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def clean(elem):
    num = elem.split(" ")[0]
    num = re.sub(",", "", num)
    return int(num)

spark = SparkSession.builder \
    .master("local") \
    .appName("census") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

df_2010 = spark.read.option("header", True).csv("s3a://continuouslearning/census_2010.csv")
df_2010 = df_2010.na.drop("any")
df_2010.createOrReplaceTempView("census_2010")

df_2020 = spark.read.option("header", True).csv("s3a://continuouslearning/census_2020.csv")
df_2020 = df_2020.na.drop("any")
df_2020.createOrReplaceTempView("census_2020")

# Register our clean function to be used on entire columns in spark.sql
spark.udf.register("cleanUDF", clean, IntegerType())

spark.sql("SELECT `Label (Grouping)` as State_2010, cleanUDF(`Total:`) as Population_2010 from census_2010 ORDER BY cleanUDF(`Total:`) DESC").createOrReplaceTempView("census_2010")
spark.sql("SELECT `Label (Grouping)` as State_2020, cleanUDF(`Total:`) as Population_2020 from census_2020 ORDER BY cleanUDF(`Total:`) DESC").createOrReplaceTempView("census_2020")

# pop_2020 - pop_2010 = diff in pop btw 2010-2020
# State, pop_2020 - pop_2010

# Query to find the difference in population between 2010 - 2020
pop_diff_df = spark.sql("SELECT State_2020 as State, Population_2020 - Population_2010 AS Diff_Pop FROM census_2010 JOIN census_2020 ON State_2010=State_2020 ORDER BY Diff_Pop DESC")

pop_diff_df.show(52)

pop_diff_df.coalesce(1).write.mode("overwrite").option("header", True).csv("s3a://continuouslearning/output")