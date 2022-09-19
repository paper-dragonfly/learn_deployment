from dash import Dash, dcc 
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import requests

app = Dash(__name__,external_stylesheets=[dbc.themes.SANDSTONE], use_pages=False)

app.layout = dbc.Container([
    dcc.Markdown('# Books!'),
    dcc.Store(id='db_bookinfo', data=None),
    dbc.Button('Get book info', id='mybtn', n_clicks=0), 
    dcc.Markdown('', id='print_db_data')
    ])

@app.callback(
    Output('print_db_data', 'children'),
    Input('mybtn', 'n_clicks')
)
def show_bookinfo(n_clicks):
    if n_clicks == 0:
        raise PreventUpdate
    if n_clicks%2 == 1:
        resp_dict = requests.get("https://learn-deploy-flaskapp.onrender.com/books").json()
    else: 
        resp_dict = {'body': 'HIDDEN'}
    return str(resp_dict['body'])

if __name__ == '__main__':
    app.run('localhost', 5011, debug=True )