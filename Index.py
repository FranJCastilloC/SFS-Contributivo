# index.py
from dash import dcc, html, Input, Output
from app import app
import dash_bootstrap_components as dbc

#Los modulos
import modules.EDE as modulo1


# La definición del sidebar usando las clases de estilo de Bootstrap y las personalizadas
sidebar = html.Div(
    [
        html.H2('Nombre del proyecto', className='display-4'),  # Asegúrate de que el nombre de la clase coincida con tu CSS
        html.Hr(),
        html.P('Menu', className='lead'),  # Asegúrate de que el nombre de la clase coincida con tu CSS
        dbc.Nav(
            [
                dbc.NavLink('Análisis Exploratorio de Datos', href='/modulo1', active='exact'),
                dbc.NavLink('Correlación de Datos', href='/modulo2', active='exact'),
                dbc.NavLink('Modelo Predictivo', href='/modulo3', active='exact'),
                dbc.NavLink('Módulo 4', href='/modulo4', active='exact'),
            ],
            vertical=True,
            pills=True,
            className='nav flex-column',  # Esta es una clase de Bootstrap, añade aquí tus propias clases si es necesario
        ),
    ],
    className='sidebar',  # Esta clase debe coincidir con el CSS
)

content = html.Div(id='page-content')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,  # Tu componente sidebar configurado previamente
    html.Div(id='page-content'),  # Asegúrate de que este id coincida con el CSS
    # ... el resto de tu layout ...
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/modulo1':
        return modulo1.layout
    elif pathname == '/modulo2':
        return modulo2.layout
    elif pathname == '/modulo3':
        return modulo3.layout
    elif pathname == '/modulo4':
        return modulo4.layout
    else:
        # Retorna algún layout predeterminado para la ruta base o para rutas no encontradas
        return html.Div('Contenido no encontrado')

if __name__ == '__main__':
    app.run_server(debug=True)