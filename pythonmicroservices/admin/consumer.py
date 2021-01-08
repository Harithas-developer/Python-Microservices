import os

import django
import pika, json, os

from products.models import Product


params = pika.URLParameters("amqps://fphdugqq:sXt6Z86Yv2RLmsjzRTIhnVBj4o357AW6@shark.rmq.cloudamqp.com/fphdugqq")

connection = pika.BlockingConnection(params)

channel =  connection.channel()

channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print('Recived in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes+1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('started consuming')
channel.start_consuming()
channel.close()