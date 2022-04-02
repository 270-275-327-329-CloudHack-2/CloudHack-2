# Code for Producer
from flask import Flask, request
import json
import pika
from uuid import uuid4

consumers = []

app = Flask(__name__)

@app.route('/new_ride', methods=['POST'])
def new_ride():
    body = json.dumps(request.form)
    task_id = 'task_' + uuid4().hex

    # Connect to rabbitmq over tcp
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    
    # Create channel to publish to ride_match queue
    channel = connection.channel()
    channel.queue_declare(queue='ride_match_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='ride_match_queue',
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
            message_id=task_id
        ))
    

    # Create new channel to publish to database queue
    channel = connection.channel()
    channel.queue_declare(queue='db_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='db_queue',
        body=body,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
            message_id=task_id
        ))

    connection.close()

    return ''


@app.route('/new_ride_matching_consumer', methods=['POST'])
def new_ride_matching_consumer():
    consumers.append({**request.form, 'ip_address': request.remote_addr})
    
    print(f'List of consumers: {consumers}', flush=True)

    return ''