from app import app
from dash import Input, Output, html
from layouts import solo_content, flex_content

@app.callback(
    Output("solo-content", "children"),
    [Input("solo-tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-single":
        return solo_content.single_layout
    elif tab_chosen == "tab-multi":
        return solo_content.multi_layout
    return html.P("This shouldn't be displayed for now...")


@app.callback(
    Output("flex-content", "children"),
    [Input("flex-tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-single":
        return flex_content.single_layout
    elif tab_chosen == "tab-multi":
        return flex_content.multi_layout
    return html.P("This shouldn't be displayed for now...")