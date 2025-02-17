# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC ## This is a Python Notebook with Functions Inside 
# MAGIC ### ```This is a Databricks notebook Source```

# COMMAND ----------

def convertFtoC(unitCol, tempCol):
    from pyspark.sql.functions import when, col
    return when(col(unitCol) == "F", (col(tempCol) - 32) * (5/9)).otherwise(col(tempCol)).alias("temp_celcius")


# COMMAND ----------

# THIS IS A BLANK CELL

# COMMAND ----------


def roundedTemp(unitCol, tempCol):
    from pyspark.sql.functions import round, concat_ws
    return concat_ws(" ", round(tempCol, 2).cast("string"), unitCol).alias("rounded_temp")
