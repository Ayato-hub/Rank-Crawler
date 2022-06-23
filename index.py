from dash import dcc, html, Input, Output

from app import app, server


from layouts import error_404, solo, flex

from callbacks import solo_graphs_callbacks,flex_graphs_callbacks, tabs_callbacks


app.layout = html.Div([
    html.Div(id='blank'), 
    dcc.Store(id='style'), 
    dcc.Location(id='url', refresh=False), 
    html.Div([
        html.Div([
            html.Div(
                className="menu", id='menu'),
        ], id='menuspace'),
        html.Div([
                html.H1('', id='dashboardtitle')
        ],className='dashboardtitle', id='title'),
    ], id = 'top_section'),
    html.Div(id='page-content', children=[])
], id='layout')


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return solo.layout
    elif pathname == '/solo':
        return solo.layout
    elif pathname == '/flex':
        return flex.layout

    else:
        return error_404.layout


@app.callback(Output('style', 'data'),
              [Input('url', 'pathname')])
def efine_styles(pathname):
    styles =[None]*2
    if pathname == '/':
        styles[0] = {'background-color': 'white', 'color': '#e07571'}
    elif pathname == '/solo':
        styles[0] = {'background-color': 'white', 'color': '#e07571'}
    elif pathname == '/flex':
        styles[1] = {'background-color': 'white', 'color': '#e07571'}
    else:
        styles=[None]*2
    return styles



@app.callback(Output('menu', 'children'),
              [Input('style', 'data')])
def change_styles(styles):
    children=[
        dcc.Link(html.Div(['Solo'], className='button_'), className='link', id='page_1', style= styles[0], href='/solo'),
        dcc.Link(html.Div(['Flex'], className='button_'), className='link', id='page_2', style= styles[1], href='/flex'),]
            
    return children



app.clientside_callback(
    """
    function(pathname) {
        if (pathname === '/') {
            document.title = 'Solo'
        } else if (pathname === '/solo') {
            document.title = 'Solo'
        }else if (pathname === '/flex') {
            document.title = 'Flex'
        }else {
            document.title = 'Page not found'
        }
    }
    """,
    Output('blank', 'children'), 
    Input('url', 'pathname')
)




if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port = 8050)

