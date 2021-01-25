# amqps://ziborigv:EGUW7o28G5N_Jj80_6cIYrAjyb8ucDwV@lionfish.rmq.cloudamqp.com/ziborigv
import pika, json

params=pika.URLParameters('amqps://ucfguvli:bIk2YhvIeWvn0PzSnbfpsFd3JOx43pXf@lionfish.rmq.cloudamqp.com/ucfguvli')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='blog', body=json.dumps(body), properties=properties)