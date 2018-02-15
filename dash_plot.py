import dash
from dash.dependencies import Input
from dash.dependencies import Output
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go
import numpy as np
import pandas as pd

# bball crawler
import aut_vinc_bballCrawler as bc


pergame = bc.getSoupFromURL('http://www.basketball-reference.com/leagues/NBA_2017_per_game.html')
pg = pergame.findAll('table')
header = []
for th in pg[0].findAll('th'):
    if not th.getText() in header:
        header.append(th.getText())
rows = pg[0].findAll('tr')[1:]  # all rows but the header
rows = [r for r in rows if len(r.findAll('td')) > 0]
parsed_table = [[col.getText() for col in row.findAll('td')] for row in rows]
ptable = pd.io.parsers.TextParser(parsed_table, names=header[1:30], index_col=0).get_chunk()

# invert the turnover metric
ptable.TOV = 1/ptable.TOV
ptable.loc[np.isinf(ptable.TOV), 'TOV'] = ptable.TOV[~np.isinf(ptable.TOV)].mean()
ptable.replace(np.nan, 0, inplace=True)
feature_vec = ['FG%','FT%','3P','TRB','AST','STL','BLK','TOV','PS/G']
print('Done pulling data and making table')
bt = pd.read_excel('autvinc_table.xlsx')
bt.tov = (1/bt.tov)*(10**3)
bt.describe()


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3('Aut Vincere Data'),

    dcc.Dropdown(
        id='drop1',
        options=[
            {'label': 'Accidental Twitter Hog', 'value': 'Accidental Twitter Hog'},
            {'label': 'Conquest Pain', 'value': 'Conquest Pain'},
            {'label': 'No Look No Pass', 'value': 'No Look No Pass'},
            {'label': 'Windy City Poohdinis', 'value': 'Windy City Poohdinis'}],
            value='Accidental Twitter Hog',),

    html.Div(id='selected-indexes'),

    dcc.Graph(
        id='fig1',
        ),
    ])


@app.callback(
        Output('fig1', 'figure'),
        [Input('drop1', 'value')])

def update_graph(input_value):
    out_df = bt[bt['team'] == input_value].mean()
    
    trace0 = go.Bar(x=list(out_df.index), y=out_df.values)
    layout = go.Layout(title='Avg values')
    return go.Figure(data=go.Data([trace0]), layout=layout)


if __name__ == '__main__':
    app.run_server(debug=True)
