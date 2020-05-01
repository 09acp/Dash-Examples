# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:47:00 2020

@author: 09ale
"""

### https://dash.plotly.com/urls
" Structuring a Multi-Page App "

import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions =  True