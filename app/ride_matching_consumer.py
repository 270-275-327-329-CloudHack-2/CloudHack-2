# Code for Ride Matching Consumer
from flask import Flask, jsonify, request
import pika
import time
import json
import os


#code for ride matching consumer
#READ CONSUMER ID AND SERVER IP FROM docker file
CONSUMER_ID = os.environ['CONSUMER_ID']
PRODUCER_ADDRESS = os.environ['PRODUCER_ADDRESS']
response = requests.post(
    f'http://{PRODUCER_ADDRESS}/new_ride_matching_consumer',
    data=f'consumer_id={CONSUMER_ID}')




def callback(ch, method, properties, body):
    body = json.loads(body.decode())
    body['_id'] = properties.message_id
    print(f'recieved {body} from ride_match queue', flush=True)

    time.sleep(int(body['time']))
    print(f' for Consumer ID: {CONSUMER_ID}, Task ID: {properties.message_id}', flush=True)

    ch.basic_ack(delivery_tag=method.delivery_tag)
    
def ride_matching_consumer():
    #RabbitMQ Client - Listen for incoming requests on the “ride_match” queue and process it.
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ride_matching_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='ride_matching_queue', on_message_callback=callback)
    channel.start_consuming()

ride_matching_consumer()


    
