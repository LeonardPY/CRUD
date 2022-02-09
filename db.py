from pymongo import MongoClient

colection = 'tkinter'
db = 'user'


def insert(arjeq):
    try:
        with MongoClient() as client:
            user_collection_db = client[colection][db]
            try:
                user_collection_db.insert_one(arjeq)
            except:
                print("db n chka")
    except:
        print("arejeqner@ chuxarkvec db")
    


def finde_name(name,pasword):
    try:
        with MongoClient() as client:  
           user_collection_db = client[colection][db]
           try:
               res = user_collection_db.find_one({'имя':name,'Пароль':pasword})
               user_id = res["_id"]
               return user_id,res
           except:
                print("user not found") 
    except:
        print("kap chhastatvec db i het")



def finde_id(Id):
    try:
        with MongoClient() as client:  
           user_collection_db = client[colection][db]
           try:
               res = user_collection_db.find_one({'_id':Id})
               return res
           except:
                print("user not found") 
    except:
        print("kap chhastatvec db i het")


def update_one(Id,query):
    try:
        with MongoClient() as client:  
           user_collection_db = client[colection][db]
           try:
               user_collection_db.update_one({'_id':Id},{"$set":query})
           except:
                print("user not found") 
    except:
        print("kap chhastatvec db i het")



def finde_meni():
    try:
        with MongoClient() as client:  
           user_collection_db = client[colection][db]
           try:
               lst = []
               users = user_collection_db.find()
               for user in users:
                   lst.append(user)
               return lst
           except:
                print("user not found") 
    except:
        print("kap chhastatvec db i het")




def delite(user_Id):
    try:
        with MongoClient() as client:  
           user_collection_db = client[colection][db]
           try:
               user_collection_db.delete_one({'_id':user_Id})

           except:
                print("user not found") 
    except:
        print("kap chhastatvec db i het") 