# Udemy-data_streamin-Project2

Using local workspace, to start zookeeper and kafka run the following commands:

> /usr/bin/zookeeper-server-start config/zookeeper.properties &  
> /usr/bin/kafka-server-start config/server.properties &

To start the kafka streamer:
> python kafka-server.py

To start spark processing:

> spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

Kafka consumer output
![Kafka Topic Info](https://github.com/nosrio/Udemy-data_streamin-Project2/blob/master/kafka-topic-info.PNG)

Crime Statistic
![Crime Statistic](https://github.com/nosrio/Udemy-data_streamin-Project2/blob/master/crime-statistic.PNG)

