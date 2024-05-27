from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

conf = SparkConf()  # create the configuration
conf.set("spark.jars", "jars/postgresql-42.7.3.jar")  # set the spark.jars

def getSparkSession():

    url_connect = 'jdbc:postgresql://127.0.0.1:5432'
    table = 'public_safety'
    mode = 'overwrite'
    properties = {
        'user': 'postgres',
        'password': 'post_pass'
    }

    sc = SparkSession.Builder() \
            .config(conf=conf) \
            .appName('pySparkProject') \
            .getOrCreate()

    return sc


