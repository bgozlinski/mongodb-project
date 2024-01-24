import os
import pika
import json
from models import Contact
from src.connect_db import MongoDBConnection
from dotenv import load_dotenv


def email_stub():
    # Stub function to simulate email sending
    pass


def callback(ch, method, properties, body):
    contact_id = json.loads(body)
    contact = Contact.objects(id=contact_id).first()
    if contact:
        email_stub()
        contact.email_sent = True
        contact.save()
        print(f"Message send do: {contact.fullname}")


current_directory = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.abspath(os.path.join(current_directory, '../../.env'))
load_dotenv(dotenv_path=dotenv_path)

# mongoDB connection
db_connection = MongoDBConnection()
db_connection.open_connection()

# RabbitMQ connection
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.getenv('HOST'),
                                                               port=5672,
                                                               credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

channel.basic_consume(
    queue='email_queue',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for messages. To exit, press CTRL+C')
channel.start_consuming()
