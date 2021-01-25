# amqps://ziborigv:EGUW7o28G5N_Jj80_6cIYrAjyb8ucDwV@lionfish.rmq.cloudamqp.com/ziborigv
import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user.settings")
django.setup()

params=pika.URLParameters('amqps://ucfguvli:bIk2YhvIeWvn0PzSnbfpsFd3JOx43pXf@lionfish.rmq.cloudamqp.com/ucfguvli')

connection=pika.BlockingConnection(params)

channel=connection.channel()

channel.queue_declare(queue='user')

def callback(ch, method, properties, body):
    print("RECEIVED IN USER")
    data = dict(json.loads(body))
    if properties.content_type == 'test_data':
        print("TEST DATA IN USER:", data)
        

channel.basic_consume(queue='user', on_message_callback=callback, auto_ack=True)

print('STARTED CONSUMING')

channel.start_consuming()
channel.close()