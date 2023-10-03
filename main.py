# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# LIBRARIES section-------------------------------------------------------------------------------------
# new modification djiaslkdjaldjal
import time
import numpy as np
import pandas as pd

import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
from dash import Input, Output, dcc, html

# REQUIREMENTS section-------------------------------------------------------------------------------------
# Load data
estudiante_df = pd.read_csv('datasets/df_estu.csv')
ingresante_df = pd.read_csv('datasets/df_ingr.csv')
matriculado_df = pd.read_csv('datasets/df_matr.csv')
grupo_programa_df = pd.read_csv('datasets/df_prgr.csv')
programa_df = pd.read_csv('datasets/df_prog_new.csv')
universidad_df = pd.read_csv('datasets/df_univ.csv')

# Generate UNIVERSITIES MAP
# Name of departamentos
departamentos = programa_df['LOCAL_DEPARTAMENTO'].unique()
options = [{'label': dep, 'value': dep} for dep in departamentos]

#
# merged_df = pd.merge(programa_df, universidad_df, on='ENTIDAD_CODIGO_INEI')
# counts_df = merged_df.groupby('LOCAL_DEPARTAMENTO')['ENTIDAD_CODIGO_INEI'].nunique().reset_index(name='counts')
# fig = px.choropleth(counts_df, locations='LOCAL_DEPARTAMENTO', locationmode='country names', color='counts',
#                     scope='south america')

# LAYOUT section-------------------------------------------------------------------------------------

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        html.Hr(),
        html.H1("Análisis de Universidades a nivel nacional"),
        html.Hr(),
        dcc.Graph(id='map-graph'),
        dcc.Dropdown(
            id='departamento-dropdown',
            options=options,
            value=departamentos[0]  # Set a default value for the dropdown
        ),
    ]
)

# CALLBACK section-------------------------------------------------------------------------------------
# Tabs creation
tab_universities_content = dbc.Card(
    dbc.CardBody(
        [

        ]
    ),
    className="mt-3",
)
tab_students_content = dbc.Card(
    dbc.CardBody(
        [

        ]
    ),
    className="mt-3",
)
tab_map_content = dbc.Card(
    dbc.CardBody(
        [

        ]
    ),
    className="mt-3",
)


# Callbacks
@app.callback(
    Output('map-graph', 'figure'),
    [Input('departamento-dropdown', 'value')]
)
def update_map(departamento):
    filtered_df = programa_df[
        programa_df['LOCAL_DEPARTAMENTO'] == departamento]  # Filter the DataFrame based on the selected department
    fig = px.scatter_mapbox(filtered_df, lat='LOCAL_LATITUD_UBICACION', lon='LOCAL_LONGITUD_UBICACION')
    fig.update_layout(mapbox_style='open-street-map')
    return fig


# MAIN section-------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
