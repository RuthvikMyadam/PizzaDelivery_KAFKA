from confluent_kafka import Producer
import json

folderName = "./"
conf = {
    'bootstrap.servers': "kafka-demo-mruthvikkumar-e6db.c.aivencloud.com:21590",
    'security.protocol': 'SSL',
    'ssl.ca.location': folderName + "ca.pem",
    'ssl.certificate.location': folderName + "service.cert",
    'ssl.key.location': folderName + "service.key"
}

producer = Producer(**conf)

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

producer.produce(
    "test-topic",
    key=json_serializer({"key": 1}),
    value=json_serializer({"message": "Hello World"})
)

producer.flush()