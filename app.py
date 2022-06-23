import dash
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd

app = dash.Dash(__name__,
suppress_callback_exceptions=True,
meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1.0, maximum-scale=1.0'}],
external_stylesheets=[dbc.themes.LUX])

server = app.server

def update_solo_data():
    cnx = sqlite3.connect('riot_api_database.db')
    df = pd.read_sql_query("SELECT * FROM RANKED_SOLO_5x5", cnx)
    cnx.close()

    df = df.rename(columns={'SummonerIndex': 'Games Played', 'SummonerName': 'Username', 
                            'SummonerId': 'ID', 'Lp': 'LP',
                            'RelativLp' : 'Relative League Points'})
    return df


def update_flex_data():
    cnx = sqlite3.connect('riot_api_database.db')
    df = pd.read_sql_query("SELECT * FROM RANKED_FLEX_SR", cnx)
    cnx.close()

    df = df.rename(columns={'SummonerIndex': 'Games Played', 'SummonerName': 'Username', 
                            'SummonerId': 'ID', 'Lp': 'LP',
                            'RelativLp' : 'Relative League Points'})
    return df


