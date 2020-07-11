from pyspark.sql import SparkSession


def main():
    spark = SparkSession.builder.appName("pyspark-docker-example").getOrCreate()

    data = [i for i in range(0, 100)]
    rdd = spark.sparkContext.parallelize(data)

    count = rdd.count()
    assert count == 100
    print(f"There are {count} data items.")


if __name__ == "__main__":
    main()
