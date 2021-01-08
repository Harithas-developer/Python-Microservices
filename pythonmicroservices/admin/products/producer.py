import pika , json

params = pika.URLParameters("amqps://fphdugqq:sXt6Z86Yv2RLmsjzRTIhnVBj4o357AW6@shark.rmq.cloudamqp.com/fphdugqq")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)