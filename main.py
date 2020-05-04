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
   SELECT DISTINCT top_scorer_name,
total_goals
FROM
 season_info
""")

top_scorer_name = []
most_goals = []


for row in cursor:
    print("Top_scorer_name:", row[0],"and his most goals:",row[1])
    top_scorer_name += [row[0]]
    most_goals += [row[1]]

data = [go.Bar(
             x=top_scorer_name,
             y=most_goals
      )]

layout = go.Layout(
    title = '',
    xaxis=dict(
        title='Top_scorer_name',
        titlefont=dict(
            family='Courier New, monospace',
            size=20,
            color='#7d7d7d'
        )
    ),
    yaxis=dict(
        title='most_goals',
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

top_scorer_most_goals = py.plot(fig, filename='top-score-most-goals')


cursor.execute( """
   SELECT DISTINCT winner_name,
  ROUND((COUNT (winner_name))/(SELECT COUNT (*) FROM season_info)*100, 2) percent
  FROM season_info
  GROUP BY winner_name
  ORDER BY percent DESC, winner_name
""")
winner_name = []
percent = []

for row in cursor:
    winner_name.append(row[0])
    percent.append(row[1])

pie_data = go.Pie(
        labels=winner_name,
        values=percent,
        title="Відсоток перемог команд відносно всіх перемог"
    )
winner_percent = py.plot([pie_data], filename='winner-percent')


cursor.execute( """
   SELECT season_year , max(goals) as goals
FROM season_info
GROUP BY season_year
ORDER BY season_year
""")

season_year = []
goals = []

for row in cursor:
    print("season_year", row[0], " goals: ", row[1])
    season_year += [row[0]]
    goals += [row[1]]

season_year_goals = go.Scatter(
    x=season_year,
    y=goals,
    mode='lines+markers'
)
data = [season_year_goals]
season_year_goals_url = py.plot(data, filename='goals_by_season_year')
my_dboard = dash.Dashboard()
top_scorer_most_goals_id = fileId_from_url(top_scorer_most_goals)
winner_percent_id = fileId_from_url(winner_percent)
season_year_goals_id = fileId_from_url(season_year_goals_url)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': top_scorer_most_goals_id,
    'title': 'Запит 1 - Вивести скільки кожен бомбардир найбільше забивав голів.'
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
    'fileId': season_year_goals_id,
    'title': 'Запит 3 - Вивести динаміку голів бомбардирів по сезонам.'
}


my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dboard, 'LaLiga')


cursor.close()
connection.close()