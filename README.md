# Udemy-data_streamin-Project2

Using local workspace, to start zookeeper and kafka run the following commands:

> /usr/bin/zookeeper-server-start config/zookeeper.properties &  
> /usr/bin/kafka-server-start config/server.properties &

To start the kafka streamer:
> python kafka-server.py

To start spark processing:

> spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py


![Crime Statistic](crime-statistic.png)

![Kafka Topic Info](kafka-topic-info.png)
