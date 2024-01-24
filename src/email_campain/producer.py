import pika
import json
import os
from models import Contact
from src.connect_db import MongoDBConnection
from faker import Faker
from src.load_dotenv import load_dotenv

load_dotenv()

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

fake = Faker()

# Faker
for _ in range(10):
    contact = Contact(fullname=fake.name(), email=fake.email())
    contact.save()

    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=json.dumps(str(contact.id))
    )

print("All messages sent to the queue.")
connection.close()
