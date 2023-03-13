import pandas as pd
import plotly.express as px
from pandas_datareader import wb

#from jupyter_dash import JupyterDash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css'
load_figure_template('bootstrap')

data = pd.read_csv("world_1960_2021.csv")
data = data.dropna()

fig_KT = px.line(
        data,
        x = 'year',
        y = "EN.ATM.CO2E.KT"
    )


fig_PC = px.line(
        data,
        x = 'year',
        y = "EN.ATM.CO2E.PC"
    )

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css])
server = app.server


app.layout = dbc.Container(
    children = [
        
        # Header
        html.H1('CO2 emissions around the world'),
        dcc.Markdown(
            """Data on emissions and potential drivers are extracted from the 
               [World Development Indicators](https://datatopics.worldbank.org/world-development-indicators/) 
               database."""
        ),
        dcc.Graph(
            figure = fig_KT,                                                    
            id = 'my_output_KT',                                               
        ),
        dcc.Graph(
            figure = fig_PC,                                                    
            id = 'my_output_PC',                                               
        ),
        
        
    ],
    className = 'dbc'
)

app.run_server(debug = True)

if __name__ == "__main__":
    app.run_server(debug = True)
