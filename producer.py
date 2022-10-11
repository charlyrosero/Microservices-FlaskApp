import json
import pika

params = pika.URLParameters('amqps://ihvqpxtq:AE_RxUBNf5_Nozs2WXmSTI330t5GST2s@beaver.rmq.cloudamqp.com/ihvqpxtq')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
    print('Published to Admin')
    print(json.dumps(body))
