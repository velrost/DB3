import csv
import cx_Oracle
username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

cursor.execute("delete from team_season_winner")
cursor.execute("delete from team")

csv_file = open('La Liga Champions.csv', encoding='utf-8', errors='ignore')
reader = csv.reader(csv_file, delimiter=',')

team_name_unique = []
for row in reader:
     team_name= row[2]
     if team_name not  in team_name_unique:
           team_name_unique.append(team_name)
     query = """insert into team(team_name) values (:team_name)"""
     cursor.execute(query, team_name=team_name)


connection.commit()
cursor.close()
connection.close()
csv_file.close()