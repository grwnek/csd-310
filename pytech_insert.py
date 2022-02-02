from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.v7vvr.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
col = db.students

shawn = {
    "student_id": "1007",
    "first_name": "Shawn",
    "last_name": "Schollenburger"
}

paul = {
    "student_id": "1008",
    "first_name": "Paul",
    "last_name": "Fuentes"
}

cameron = {
    "student_id": "1009",
    "first_name": "Cameron",
    "last_name": "Clonemonster"
}

shawn_id = db.students.insert_one(shawn).inserted_id
paul_id = db.students.insert_one(paul).inserted_id
cameron_id = db.students.insert_one(cameron).inserted_id

print("-- INSERT STATEMENTS --")
print("Inserted student record Shawn Schollenburger into the students collection with document id:")
print(shawn_id)
print("Inserted student record Paul Fuentes into the students collection with document id:")
print(paul_id)
print("Inserted student record Cameron Clonemaster into the students collection with document id:")
print(cameron_id)
print("End of program, press any key to exit...")