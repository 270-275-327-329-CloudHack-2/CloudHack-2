# Use this file to setup the database consumer that stores the ride information in the database
import pika

def database_consumer():
    # Connect to the database
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='db_queue', durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='db_queue', on_message_callback=callback)
    channel.start_consuming()

