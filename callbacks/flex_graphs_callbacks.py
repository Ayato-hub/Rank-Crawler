from app import app
from dash import Input, Output, dcc
import plotly.express as px


from app import update_flex_data

@app.callback(
    Output('flex-single-line-graph', 'children'),
    [Input('flex-single-players', 'value'),
     Input('flex-single-interval', 'n_intervals')]
)
def show_line(value, n_intervals):

    df = update_flex_data()

    filtered_df = df[df['Username'] == value]
    fig = px.line(filtered_df, x='Games Played', y='Relative League Points', color='Username', markers=True,
                  hover_name='Username', hover_data=['Username', 'Date', 'Division', 'Tier', 'LP'])
    fig.update_layout(title='Users Relative League Points', title_x=0.5, plot_bgcolor='#1f2c56',
                      paper_bgcolor='#1f2c56', font_color='white')
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_traces(line_color='#c05a62', hovertemplate='<b>%{customdata[0]}</b><br><br>' +
                      '<b>Username:</b> %{customdata[0]}<br>' +
                      "<b>Date:</b> %{customdata[1]}<br>" +
                      "<b>Division:</b> %{customdata[2]}<br>" +
                      "<b>Tier:</b> %{customdata[3]}<br>" +
                      "<b>LP:</b> %{customdata[4]}<br>" +
                      '<br><extra></extra>')
    return dcc.Graph(figure=fig)




@app.callback(
    Output('flex-multi-line-plot', 'children'),
    [Input('flex-multi-interval', 'n_intervals')]
)
def show_graph(none):

    df = update_flex_data()

    fig = px.line(df, x='Games Played', y='Relative League Points', color='Username', markers=True,
                  hover_name='Username', hover_data=['Username', 'Date', 'Division', 'Tier', 'LP'])
    fig.update_layout(title='Users Relative League Points', title_x=0.5, plot_bgcolor='#1f2c56',
                      paper_bgcolor='#1f2c56', font_color='white')
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)
    fig.update_traces(hovertemplate='<b>%{customdata[0]}</b><br><br>' +
                      '<b>Username:</b> %{customdata[0]}<br>' +
                      "<b>Date:</b> %{customdata[1]}<br>" +
                      "<b>Division:</b> %{customdata[2]}<br>" +
                      "<b>Tier:</b> %{customdata[3]}<br>" +
                      "<b>LP:</b> %{customdata[4]}<br>" +
                      '<br><extra></extra>')
    return dcc.Graph(
        figure=fig,
        animate=True
    )