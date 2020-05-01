# -*- coding: utf-8 -*-
"""
Created on Fri May  1 18:00:04 2020

@author: 09ale
"""

# https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

import dash_bootstrap_components as dbc
import dash_html_components as html

row = html.Div(
    [
        dbc.Row(dbc.Col(html.Div("A single column"))),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns")),
            ]
        ),
    ]
)