from pyspark import SparkContext,RDD
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer
import os
import findspark
from elasticsearch import Elasticsearch
import nltk
#nltk.download('all')
from nltk.corpus import stopwords
import streamz
import json
from pyspark.sql import SQLContext

es = Elasticsearch(hosts='ec2-54-225-43-20.compute-1.amazonaws.com:9200')

findspark.init('D:\Rcg\spark\spark-2.4.3-bin-hadoop2.7\spark-2.4.3-bin-hadoop2.7\spark-2.4.3-bin-hadoop2.7')

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.3 pyspark-shell'

# Create a local StreamingContext with two working thread and batch interval of 1 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)
kafkastream = KafkaUtils.createStream(ssc, 'ec2-54-225-43-20.compute-1.amazonaws.com:2181', 'mygroup', {'talend_topics': 1})
lines = kafkastream.map(lambda x: x[1])
#
# lines.pprint()

# for x in lines:
#     es.index(index="spark_test",
#                            doc_type="test-type",
#                            body={"marketplace": str(lines["marketplace"][x])})
#
# top_five_authors = lines.transform\
#   (lambda rdd:sc.parallelize(rdd.take(5)))


# top_five_authors = lines.transform\
#   (lambda rdd:sc.parallelize(rdd.take(2)))
# filtered_authors = lines.filter(lambda x:x[0].lower().startswith('j'))
# filtered_authors.pprint()
# top_five_authors.pprint()
#

x = SQLContext.



ssc.start()
ssc.awaitTermination()

