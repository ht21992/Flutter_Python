
from bson.objectid import ObjectId
from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")
dbname = client['bookstore']
collection = dbname['books']


def update_fav_by_id(id, current_value: bool):
    query = {"_id": ObjectId(id)}
    newvalues = {"$set": {"fav": not current_value}}
    collection.update_one(query, newvalues)


def get_books():
    books = collection.find({})
    return books


def get_favs():
    query = {"fav": True}
    fav_books = collection.find(query)
    return fav_books


def search_by_title(title: str):
    query = {"title": {"$regex": title, '$options': 'i'}}

    books = collection.find(query)

    return books


def add_book(title: str, author: str, country: str, imageLink: str, language: str, link: str, pages: str, year: str):
    try:
        query = {'author': author, 'country': country, 'imageLink': f"images/{imageLink.replace(' ', '_')}", 'language': language, 'link': link, 'pages': int(pages), 'title':
                 title, 'year': int(year), 'fav': False}
        collection.insert_one(query)
        return f"{title} has been successfully added to the library", True
    except Exception as e:
        return 'Please check your inputs', False
