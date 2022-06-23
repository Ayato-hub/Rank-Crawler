import dash_bootstrap_components as dbc
from dash import html, dcc
import numpy as np

from app import update_solo_data


df = update_solo_data()

mycustomdata = np.stack((df['Date'], df['Games Played'], df['Username'], df['ID'], df['Division'],
                         df['Tier'], df['LP'], df['Relative League Points']), axis=-1)


multi_layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.Div(id='solo-multi-line-plot', className='card-container twelve column'), width=12, style={'margin_top': '50px'}),
    ),
    dbc.Row(
        dbc.Col([
            dcc.Interval(
                id='solo-multi-interval',
            interval=1*60000
            )
        ])
    )
], fluid=True)


single_layout = html.Div([
    dbc.Row([
        dbc.Col(
            [
                dcc.Dropdown(
                    id="solo-single-players",
                    multi=False,
                    value=df['Username'][0],
                    options=[
                        {"label": i, "value": i} for i in df['Username'].unique()
                    ],
                    clearable=False,
                    style={'background-color': '#1f2c56',
                           'color': 'white', 'margin-top': '10px'}
                ),
                dcc.Interval(
                    id='solo-single-interval',
                    interval = 1*60000,
                )
            ],
            width=12,
            style={'margin-bottom': '20px'}
        ),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='solo-single-line-graph')
        ])
    ])
])