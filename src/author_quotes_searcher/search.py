from models import Quote, Author
from connect_db import MongoDBConnection


def search_quotes():
    db_connection = MongoDBConnection()
    db_connection.open_connection()

    while True:
        command = input("Enter your command: ").strip()
        if command.lower() == "exit":
            db_connection.close_connection()
            break

        if ':' not in command:
            print("Invalid command format. Please use 'key: value'.")
            continue

        key, value = command.split(':', 1)
        key = key.strip()
        value = value.strip()

        if key == "name":
            author = Author.objects(fullname=value).first()
            if not author:
                print(f"No author found with the name '{value}'")
                continue

            quotes = Quote.objects(author=author)
        elif key == "tag":
            quotes = Quote.objects(tags=value)
        elif key == "tags":
            tags = value.split(',')
            tags = [tag.strip() for tag in tags]  # Trim spaces from each tag
            quotes = Quote.objects(tags__in=tags)
        else:
            print("Invalid command.")
            continue

        if quotes:
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"No quotes found for {key}: '{value}'")


search_quotes()
