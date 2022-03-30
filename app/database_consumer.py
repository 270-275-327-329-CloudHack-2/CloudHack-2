# Use this file to setup the database consumer that stores the ride information in the database
import pika
from pymongo import MongoClient

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # Store the data in the database
    # ...

    ch.basic_ack(delivery_tag = method.delivery_tag)

def database_consumer(payload):
    # Connect to the database
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='db_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='db_queue', on_message_callback=callback)
    channel.start_consuming()
    uri = "mongodb+srv://paul:123No4321!@cluster0.uviuy.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(uri)

    db = client["Rides"]

    Collection = db["deets"]
    
    if isinstance(payload, list):
        Collection.insert_many(payload)
    else:
	    Collection.insert_one(payload)

if __name__ == '__main__':
    payload = {
        "ABS":"test",
        "name":"joy"
        
    }
    database_consumer(payload)