# Code for Producer
from multiprocessing import connection
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
        routing_key='ride_matching_queue',
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
def new_ride_matching_consumer(map):
    #This will be listening to POST requests from new consumers that contains the consumer_id and store their IP address and name. The Name and IP address will just be stored as a map, in an array, where each map has name and IP as the keys, and the consumer_id and the request IP as the values
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='ride_matching_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='ride_matching_queue',
        body= map,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    return jsonify({'message': 'IP and Name added'})
    


#A RabbitMQ client to create queues and send the data to consumers. The RabbitMQ client in the producer will register a new queue each for the ride-sharing consumer microservice and one for the database microservice, and will be responsible for sending out the data from the POST requests to consumers



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


