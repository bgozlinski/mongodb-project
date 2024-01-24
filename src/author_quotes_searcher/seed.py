from src.connect_db import MongoDBConnection
from models import Author, Quote
import json


def upload_data():
    db_connection = MongoDBConnection()
    db_connection.open_connection()
    # Load authors
    with open('json/authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            author = Author.objects(fullname=author_data['fullname']).first()
            if not author:
                author = Author(**author_data)
                author.save()

    # Load quotes
    with open('json/quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author = Author.objects(fullname=quote_data['author']).first()
            if author:
                quote = Quote(quote=quote_data['quote'], author=author, tags=quote_data['tags'])
                quote.save()

upload_data()
