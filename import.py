import csv
import cx_Oracle
import io
username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

cursor.execute("delete from human_season")
cursor.execute("delete from team_season_winner")
cursor.execute("delete from season")
cursor.execute("delete from team")
cursor.execute("delete from human")
cursor.execute("delete from human_season")

csv_file = io.open('La Liga Champions.csv', encoding='utf-8')
reader = csv.reader(csv_file, delimiter=',')

team_name_unique = []
human_name_unique = []
season_year_unique = []
for row in reader:
     team_name = row[3]
     human_name = row[5]
     season_year = row[1]
     if team_name not in team_name_unique:
         team_name_unique.append(team_name)
         query = """insert into team(team_name) values (:team_name)"""
         cursor.execute(query, team_name=team_name)
     if human_name not in human_name_unique:
         human_name_unique.append(human_name)
         query1 = """insert into human(human_name) values (:human_name)"""
         cursor.execute(query1, human_name=human_name)
     if season_year not in season_year_unique:
         season_year_unique.append(season_year)
         query2 = """insert into season(season_year) values (:season_year)"""
         cursor.execute(query2, season_year=season_year)
         query3 = """insert into team_season_winner(team_name_fk, season_year_fk) values (:team_name, :season_year)"""
         cursor.execute(query3, team_name=team_name, season_year=season_year)
         query4 = """insert into human_season(human_name_fk , season_year_fk) values (:human_name, :season_year)"""
         cursor.execute(query4, human_name=human_name, season_year=season_year)

connection.commit()
cursor.close()
connection.close()
csv_file.close()
