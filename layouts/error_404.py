from dash import html

layout = html.Div([html.H1('Error 404!', style = {'color': 'red'}), 
html.P('Please select a page from the menu above.')], 
style = {'height':'80vh',
         'width': '90vw',
         'display': 'flex',
         'flex-direction': 'column',
         'justify-content': 'center',
         'align-items': 'center',
         'color': 'white'})