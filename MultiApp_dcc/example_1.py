# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:06:35 2020

@author: 09ale
"""


# https://dash.plotly.com/urls


import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Tabs([
            # tab1 
            dcc.Tab(label="TAB 1", 
                children=[
                    dcc.Location(id='url', refresh=False),
                    html.Div(id='page-content')
            ]),

            # tab2 
            dcc.Tab(label="TAB 2", 
                children=[
                    html.H1("PAGES UNDER SECOND TAB"),
                    dcc.Location(id='url-t2', refresh=False),
                    html.Div(id='page-content-t2')
                    
            ]),            
    ]),
])

# MULTIPLE PAGES WITHIN A SINGLE TAB
index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])



############ TAB 1 
# ELEMENTS PAGE 1 - Not in app layout section
page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Dropdown(
        id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='page-1-content'),
    html.Br(),
    # URL 1 - for display_page callback
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    # URL 2 - for display_page callback
    dcc.Link('Go back to home', href='/'),
])

@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('page-1-dropdown', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)
page_2_layout = html.Div([
    html.H1('Page 2'),
    # ELEMENT AND DATA
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content', 'children'),
              [dash.dependencies.Input('page-2-radios', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
# CONTENT DISPLAYED ACCORDING TO URL
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


############ TAB 2 - adding elements here too
# ELEMENTS PAGE 1 - Not in app layout section
page_1_layout_t2 = html.Div([
    html.H1('Page 1 TAB2'),
    dcc.Dropdown(
        id='page-1-dropdown-t2',
        options=[{'label': i, 'value': i} for i in ['AAA', 'BBB', 'CCC']],
        value='BBB'
    ),
    html.Div(id='page-1-content-t2'),
    html.Br(),
    # URL 1 - for display_page callback
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    # URL 2 - for display_page callback
    dcc.Link('Go back to home', href='/'),
])


# PAGE 1
@app.callback(dash.dependencies.Output('page-1-content-t2', 'children'),
              [dash.dependencies.Input('page-1-dropdown-t2', 'value')])
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)
page_2_layout_t2 = html.Div([
    html.H1('Page 2 TAB2 '),
    # ELEMENT AND DATA
    dcc.RadioItems(
        id='page-2-radios-t2',
        options=[{'label': i, 'value': i} for i in ['RED', 'RED2', 'RED3']],
        value='RED'
    ),
    html.Div(id='page-2-content-t2'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])

@app.callback(dash.dependencies.Output('page-2-content-t2', 'children'),
              [dash.dependencies.Input('page-2-radios-t2', 'value')])
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

# Update the index
@app.callback(dash.dependencies.Output('page-content-t2', 'children'),
              [dash.dependencies.Input('url-t2', 'pathname')])
# CONTENT DISPLAYED ACCORDING TO URL
def display_page_t2(pathname):
    if pathname == '/page-1':
        return page_1_layout_t2     # UPDATE
    elif pathname == '/page-2':
        return page_2_layout_t2     # UPDATE
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

if __name__ == '__main__':
    app.run_server(debug=False)