from dash import html
import dash_bootstrap_components as dbc


app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Single Player", tab_id="tab-single", tab_style = {'margin-left' : '230px'},
                        labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(label="Multiple Players", tab_id="tab-multi", tab_style = {'margin-left' : '230px'},
                        labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ],
            id="solo-tabs",
            active_tab="tab-single",
        ),
    ], className="mt-3"
)

layout = dbc.Container([
    dbc.Row(dbc.Col(html.H2("Rank Crawler Solo",
                            style={"textAlign": "center", 'color' : 'white'}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='solo-content', children=[])

])