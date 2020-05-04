import cx_Oracle
import re
import chart_studio
from plotly import graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash

chart_studio.tools.set_credentials_file(username='vel.rost7', api_key='bMc1Mt0Mg5OHVvI4uqjj')

def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.0-9]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

username = 'velrost'
password = 'Richbitch8228'
database = 'localhost:1521/xe'

connection = cx_Oracle.connect(username, password, database)
cursor = connection.cursor()

cursor.execute("""
   SELECT DISTINCT 
 team_name_fk,
 season_year
FROM
 season_info1
""")


team_name_fk = []
season_year = []


for row in cursor:
    print("eam_name:", row[0],"and season year:",row[1])
    team_name_fk += [row[0]]
    season_year += [row[1]]

data = [go.Bar(
             x=team_name_fk,
             y=season_year
      )]

layout = go.Layout(
    title = '',
    xaxis=dict(
        title='Team_name',
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    ),
    yaxis=dict(
        title='season_year',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    )
)

fig = go.Figure(data=data, layout=layout)

team_name_fk_season_year = py.plot(fig, filename='team-name-season-year')


cursor.execute("""
   SELECT DISTINCT team_name_fk,
  ROUND((COUNT (team_name_fk))/(SELECT COUNT (*) FROM season_info1)*100, 2) percent
  FROM season_info1
  GROUP BY team_name_fk
  ORDER BY percent DESC, team_name_fk
""")
team_name_fk = []
percent = []

for row in cursor:
    team_name_fk.append(row[0])
    percent.append(row[1])

pie_data = go.Pie(
        labels=team_name_fk,
        values=percent,
        title="Відсоток перемог команд відносно всіх перемог"
    )
winner_percent = py.plot([pie_data], filename='winner-percent')


cursor.execute( """
   SELECT season_year, human_name_fk
   FROM season_info1
   ORDER BY season_year
""")

season_year = []
human_name_fk = []

for row in cursor:
    print("season_year", row[0], " human_name: ", row[1])
    season_year += [row[0]]
    human_name_fk += [row[1]]

season_year_human_name = go.Scatter(
    x=season_year,
    y=human_name_fk,
    mode='lines+markers'
)
data = [season_year_human_name]
season_year_human_name_url = py.plot(data, filename='human_name_season_year')
my_dboard = dash.Dashboard()
team_name_fk_season_year_id = fileId_from_url(team_name_fk_season_year)
winner_percent_id = fileId_from_url(winner_percent)
season_year_human_name_id = fileId_from_url(season_year_human_name_url)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': team_name_fk_season_year_id,
    'title': 'Запит 1 - Вивести яка команда і в якому році ставала переможцем.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': winner_percent_id,
    'title': 'Запит 2 - Вивести відсоток перемог кожної команди від  загальної кількості.'

}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': season_year_human_name_id,
    'title': 'Запит 3 - Вивести динаміку зміни бомбардирів по сезонам'
}


my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'LaLiga')


cursor.close()
connection.close()