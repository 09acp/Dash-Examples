# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:04:45 2020

@author: 09ale
"""

# =============================================================================
#   Choropath figure code and data 
#   https://plotly.com/python/choropleth-maps/
# 
#   Adding to Dash
#   https://towardsdatascience.com/build-an-interactive-choropleth-map-with-plotly-and-dash-1de0de00dce0
# =============================================================================

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar = {"thickness": 10, "len": 0.5}, #, "x": 0.8, "y": 0.6, 
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))

fig.update_layout(
    title_text='2014 Global GDP',
    height = 600,
    #width = 1000,
    geo=dict(
        showframe=True,
        showcoastlines=False,
        projection_type= 'equirectangular'#'natural earth' #
    ),
#    annotations = [dict(
#        x=0.55,
#        y=0.1,
#        xref='paper',
#        yref='paper',
##        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
##            CIA World Factbook</a>',
#        showarrow = False
#    )]
)

#fig.show()

# =============================================================================
#   Code for Dash Browser App   
# =============================================================================

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=False)