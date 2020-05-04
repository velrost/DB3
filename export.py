import cx_Oracle
import csv
import io
username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)

cursor = connection.cursor()

cursor.execute("""
SELECT team_name, season_year, human_name 
FROM season
INNER JOIN team_season_winner USING(season_year_fk)
INNER JOIN human_season USING(season_year_fk) """)

with io.open('text.csv', "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow('season_year, team_name, human_name'.split(","))
        for row in cursor:
            string = ','.join(map(str, row))
            writer.writerow(string.split(","))

cursor.close()
