import cx_Oracle
import csv
import io
username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)

cursor = connection.cursor()

cursor.execute("""
SELECT DISTINCT
season.season_year,
human_season.human_name_fk,
team_season_winner.team_name_fk
FROM
season
INNER JOIN human_season ON season.season_year=human_season.season_year_fk
INNER JOIN team_season_winner ON season.season_year=team_season_winner.season_year_fk""")

with io.open('text.csv', "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow('season_year, team_name, human_name'.split(","))
        for row in cursor:
            string = ','.join(map(str, row))
            writer.writerow(string.split(","))

cursor.close()