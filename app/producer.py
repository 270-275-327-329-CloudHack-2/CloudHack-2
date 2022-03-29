# Code for Producer
from flask import Flask, jsonify, request
import pika

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/new_ride', methods=['POST'])
def new_ride(payload):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ride_matching_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body= payload,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    channel.queue_declare(queue='db_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='db_queue',
        body= payload,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return jsonify({'message': 'Ride added'})


@app.route('/new_ride_matching_consumer', methods=['POST'])
def new_ride_matching_consumer(payload):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body= payload,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return " [x] Sent: %s" % payload

#A RabbitMQ client to create queues and send the data to consumers. The RabbitMQ client in the producer will register a new queue each for the ride-sharing consumer microservice and one for the database microservice, and will be responsible for sending out the data from the POST requests to consumers



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


