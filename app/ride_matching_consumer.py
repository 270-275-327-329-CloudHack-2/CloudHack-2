# Code for Ride Matching Consumer
from flask import Flask, jsonify, request
import pika
import time
import json


#code for ride matching consumer
#READ CONSUMER ID AND SERVER IP FROM docker file





def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.time)
    #Store the data in the database
    #...
    #print task id and customer id
   
    ch.basic_ack(delivery_tag = method.delivery_tag)
    
def ride_matching_consumer():
    #RabbitMQ Client - Listen for incoming requests on the “ride_match” queue and process it.
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ride_matching_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='ride_matching_queue', on_message_callback=callback)
    channel.start_consuming()


    
