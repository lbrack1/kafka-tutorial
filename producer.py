from kafka import KafkaProducer

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'my-topic-three'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

producer.send(topicName, b'Hello World!')
producer.flush()
