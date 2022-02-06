from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v7vvr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech


firstnames = db.students.find({}, { "first_name": 1 })
lastnames = db.students.find({}, { "last_name": 1 })
studentids = db.students.find({}, { "student_id": 1 })

docs = db.students.find({}, { "student_id": 1, "first_name": 1, "last_name": 1 })
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for firstname in firstnames:
    print(firstname)

for lastname in lastnames:
    print(lastname)

for studentid in studentids:
    print(studentid)

result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "S."}})

print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
pupils = db.students.find_one({"student_id": "1007"})
print(pupils)