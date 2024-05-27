from pyspark.sql import SparkSession
from pyspark.conf import SparkConf

import constants as c


def holder():
    conf = get_conf()

    sc = SparkSession.Builder() \
        .config(conf=conf) \
        .appName('pySparkProject') \
        .getOrCreate()


def get_conf():
    conf = SparkConf()  # create the configuration
    conf.set('spark.jars', c.POSTGRES_JAR)

    return conf
