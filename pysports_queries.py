from errno import errorcode
import mysql.connector
from  mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Lego_Las49",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
    

cursor = db.cursor()
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team name: {}".format(team[1]))

cursor.execute("SELECT first_name, last_name, team_id FROM player")
players = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --")
for player in players:
    print("Player name: {}".format(player[1]))

