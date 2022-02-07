from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v7vvr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech


firstnames = db.students.find({}, { "first_name": 1 })
lastnames = db.students.find({}, { "last_name": 1 })
studentids = db.students.find({}, { "student_id": 1 })

print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for firstname in firstnames:
    print(firstname)

for lastname in lastnames:
    print(lastname)

for studentid in studentids:
    print(studentid)

peter = {
    "student_id": "1010",
    "first_name": "Peter",
    "last_name": "Piper"
}

peter_id = db.students.insert_one(peter).inserted_id

print("Inserted student record Peter Piper into the students collection with document id:")
print(peter_id)
print("-- DISPLAYING STUDENT TEST DOC")

pupils = db.students.find_one({"student_id": "1010"})
print(pupils)

result = db.students.delete_one({ "student_id": "1010" })

firstnames = db.students.find({}, { "first_name": 1 })
lastnames = db.students.find({}, { "last_name": 1 })
studentids = db.students.find({}, { "student_id": 1 })

print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for firstname in firstnames:
    print(firstname)
for lastname in lastnames:
        print(lastname)
for studentid in studentids:
    print(studentid)