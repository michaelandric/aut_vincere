import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown(
        id='drop1',
        options=[
            {'label': 'Accidental Twitter Hog', 'value': 'Accidental Twitter Hog'},
            {'label': 'Conquest Pain', 'value': 'Conquest Pain'},
            {'label': 'No Look No Pass', 'value': 'No Look No Pass'},
            {'label': 'Windy City Poohdinis', 'value': 'Windy City Poohdinis'}],
            value='Accidental Twitter Hog',),
    
    html.Div(id='output-container')
])


@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('drop1', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
