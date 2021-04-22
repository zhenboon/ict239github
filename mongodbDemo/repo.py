import pymongo
connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['lab2demo']

def read_menu():
    return db.menu.find({})

def create_menu(name, ratings):
    assert name is not None
    #assert numfeedback is not None

    db.menu.insert_one({'dishes':name,'ratings':ratings})


def update_menu(name, new_ratings):
    assert name is not None
    #assert new_numfeedback is not None

    db.menu.update_one({'dishes':name},{'$set':{'ratings':new_ratings}})

def delete_menu(name):
    assert name is not None

    db.menu.delete_one({'dishes':name})

