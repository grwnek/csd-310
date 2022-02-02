from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v7vvr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students

docs = db.students.find({}, { "student_id": 1, "first_name": 1, "last_name": 1 })
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for doc in docs:
    print(doc)

print("-- DISPLAYING STUDENTS FROM find_one QUERY --")
pupils = db.students.find_one({"student_id": "1007"})
print(pupils)