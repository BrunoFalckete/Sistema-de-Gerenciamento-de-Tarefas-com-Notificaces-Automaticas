import os
from pymongo import MongoClient

def get_db():
    # Para MongoDB local use a string abaixo
    client = MongoClient('mongodb+srv://kqPcqSy46Dg8:<db_password>@cluster0.doax7a5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    
    # Para usar o MongoDB Atlas, substitua pela string de conexão fornecida
    # client = MongoClient(os.getenv("MONGODB_URI"))

    db = client['task_manager_db']
    return db
