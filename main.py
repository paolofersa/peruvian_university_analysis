# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
# LIBRARIES section-------------------------------------------------------------------------------------
import time
import numpy as np
import pandas as pd

import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash import Input, Output, dcc, html

# REQUIREMENTS section-------------------------------------------------------------------------------------
# Load data
df_estu = pd.read_csv('datasets/df_estu.csv')
df_ingr = pd.read_csv('datasets/df_ingr.csv')
df_matr = pd.read_csv('datasets/df_matr.csv')
df_prgr = pd.read_csv('datasets/df_prgr.csv')
df_prog = pd.read_csv('datasets/df_prog.csv')
df_univ = pd.read_csv('datasets/df_univ.csv')

# Get unique values
departamentos = df_prog['LOCAL_DEPARTAMENTO'].unique()
options = [{'label': dep, 'value': dep} for dep in departamentos]

# LAYOUT section-------------------------------------------------------------------------------------

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dcc.Store(id="store"),
        html.Hr(),
        html.H1("Análisis de Universidades a nivel nacional"),
        html.Hr(),
        dbc.Button(
            "Regenerate graphs",
            color="primary",
            id="button",
            className="mb-3",
        ),
        dbc.Tabs(
            [
                dbc.Tab(label="Scatter", tab_id="scatter"),
                dbc.Tab(label="Histograms", tab_id="histogram"),
                dbc.Tab(label="Map", tab_id="map"),
            ],
            id="tabs",
            active_tab="scatter",
        ),
        html.Div(id="tab-content", className="p-4"),
    ]
)


# CALLBACK section-------------------------------------------------------------------------------------
# Tabs creation
tab_scatter_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.Graph(figure=data["scatter"]),
        ]
    ),
    className="mt-3",
)
tab_histogram_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Col(dcc.Graph(figure=data["hist_1"]), width=6),
            dbc.Col(dcc.Graph(figure=data["hist_2"]), width=6),
        ]
    ),
    className="mt-3",
)
tab_map_content = dbc.Card(
    dbc.CardBody(
        [
            d
        ]
    ),
    className="mt-3",
)


@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab and data is not None:
        if active_tab == "scatter":
            return tab_scatter_content
        elif active_tab == "histogram":
            return tab_histogram_content
        elif active_tab == "map":
            return tab_map_content
    return "No tab selected"


@app.callback(Output("store", "data"), [Input("button", "n_clicks")])
def generate_graphs(n):
    """
    This callback generates three simple graphs from random data.
    """
    if not n:
        # generate empty graphs when app loads
        return {k: go.Figure(data=[]) for k in ["scatter", "hist_1", "hist_2"]}

    # simulate expensive graph generation process
    time.sleep(2)

    # generate 100 multivariate normal samples
    data = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

    scatter = go.Figure(
        data=[go.Scatter(x=data[:, 0], y=data[:, 1], mode="markers")]
    )
    hist_1 = go.Figure(data=[go.Histogram(x=data[:, 0])])
    hist_2 = go.Figure(data=[go.Histogram(x=data[:, 1])])

    # save figures in a dictionary for sending to the dcc.Store
    return {"scatter": scatter, "hist_1": hist_1, "hist_2": hist_2}


# MAIN section-------------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, port=8888)
