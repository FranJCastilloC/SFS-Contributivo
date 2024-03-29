from dash import html, dcc
import plotly.express as px
import pandas as pd

# Asegúrate de que cada '[' tenga su ']' correspondiente.
layout = html.Div([
    html.H3('Análisis Exploratorio de Datos'),

    html.Div([
        html.H4('Resumen Estadístico'),
        dcc.Markdown(id='resumen-estadistico'),
       
    ]), 
])  