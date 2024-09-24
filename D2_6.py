# 1 Importing all necessary libraries
import dash
import sys
from dash import dash_table
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px
import plotly.figure_factory as ff

from dash.dependencies import Input, Output

import pandas as pd
from dash import html

from plot_functions3 import *


# 2 Importing the data
mf = pd.read_excel('sales_data_sample.xlsx')

# Preprocessing Territory field
mf_t = 'TERRITORY'
mf[mf_t].fillna('NA', inplace=True)


l1_v = 'STATUS'
l1_d = list(mf[l1_v].unique())
l1_d.sort()

l2_v = 'COUNTRY'
l2_d = list(mf[l2_v].unique())
l2_d.sort()

l3_v = 'TERRITORY'
l3_d = list(mf[l3_v].unique())
l3_d.sort()

l4_v = 'CITY'
l4_d = list(mf[l4_v].unique())
l4_d.sort()

#c2_d = 'COUNTRY'

external_stylesheets = [dbc.themes.BOOTSTRAP]
# 3. Making HTML Layout
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 
#app = JupyterDash(__name__)

app.layout = html.Div(children = [
    # Title
    #html.H1('Sales Data Analysis',
    #        style = {'textAlign': 'center','color' : '#503D36','font-size': '40px'}),
    
    
    
    html.Div([
        
        dbc.Row([
          # First row section of screen
            dbc.Col(
                html.Div([
                    #html.Div(['Status: ', dcc.Input(id = 'status', value = 'Shipped', type ='text', style = {'height':20, 'font-size': 17})], style={'font-size': 17}),
                    html.Div(['Status: ', dcc.Dropdown(id = 'status', options = [{'label': i, 'value': i} for i in l1_d], value = None, style = {'height':40, 'width': 250,'font-size': 22})], style={'font-size': 22}),
                    #html.Br(),
                    html.Div(dcc.Graph(id = 'Horizontal_BarChart', clear_on_unhover=True))],
                    style = {'textAlign': 'center'}
                    ), width = 3),

            dbc.Col(
                html.Div([
                    #html.Div(['Country: ', dcc.Input(id = 'country', value = 'USA', type ='text', style = {'height':20, 'font-size': 17})], style={'font-size': 20}),
                    html.Div(['Country: ', dcc.Dropdown(id = 'country', options = [{'label': i, 'value': i} for i in l2_d], value = None, style = {'height':40, 'width': 250, 'font-size': 22})], style={'font-size': 22}),
                    #html.Br(),
                    html.Div(dcc.Graph(id = 'TreeMap0', clear_on_unhover=True))],
                    style = {'textAlign': 'center'}
                    ), width=3),

            dbc.Col(
                html.Div([
                    #html.Div(['Territory: ', dcc.Input(id = 'territory', value = 'NA', type ='text', style = {'height':20, 'font-size': 17})], style={'font-size': 20}),
                    html.Div(['Territory: ', dcc.Dropdown(id = 'territory', options = [{'label': i, 'value': i} for i in l3_d], value = None, style = {'height':40, 'width': 250, 'font-size': 22})], style={'font-size': 22}),
                    #html.Br(),
                    html.Div(dcc.Graph(id = 'TreeMap1', clear_on_unhover = True))],
                    style = {'textAlign': 'center'}
                    ), width=3),

            dbc.Col(
                html.Div([
                    #html.Div(['City: ', dcc.Input(id = 'city', value = 'Aaarhus', type ='text', style = {'height':20, 'font-size': 17})], style={'font-size': 20}),
                    html.Div(['City: ', dcc.Dropdown(id = 'city', options = [{'label': i, 'value': i} for i in l4_d], value = None, style = {'height':40, 'width': 250, 'font-size': 22})], style={'font-size': 22}),
                    #html.Br(),
                    html.Div(dcc.Graph(id = 'PieChart', clear_on_unhover = True))],
                    style = {'textAlign': 'center'}
                    ), width=3),
        ],
        ),
         ]),
    
    # Second Row Section in Screen
    html.Div(
            [
                html.Div([], style={'height': 200, 'width':20}),

                html.Div(html.Div(id = 'Table0'), style = {'height': 200, 'width': 600}),
                
                #html.Div([], style={'height': 200, 'width':20}),
                
                html.Div(html.Div(id='Table1'), style = {'height': 200, 'width': 1000})
                
            ], style = {'display': 'flex', })
            
])



# Variables for Filtering

# Dropdown Variables
drp_v1 = 'STATUS'
drp_v2 = 'COUNTRY'
drp_v3 = 'TERRITORY'
drp_v4 = 'CITY'

# Variables from the charts
bar_v = 'PRODUCTLINE'
tm0_v = 'CITY'
tm1_v = 'CITY'
pc_v = 'DEALSIZE'

# Function & Call Back Section

@app.callback(
    [Output(component_id = 'Horizontal_BarChart', component_property = 'figure'),
     Output(component_id = 'TreeMap0', component_property = 'figure'),
     Output(component_id = 'TreeMap1', component_property = 'figure'),
     Output(component_id = 'PieChart', component_property = 'figure'),
     Output(component_id = 'Table0', component_property = 'children'),
     Output(component_id = 'Table1', component_property = 'children')
    ],
    [
     Input(component_id = 'status', component_property = 'value'),
     Input(component_id = 'country', component_property = 'value'),
     Input(component_id = 'territory', component_property = 'value'),
     Input(component_id = 'city', component_property = 'value'),
     Input(component_id = 'Horizontal_BarChart', component_property = 'hoverData') ,
     Input(component_id = 'TreeMap0', component_property = 'hoverData'),
     Input(component_id = 'TreeMap1', component_property = 'hoverData'),
     Input(component_id = 'PieChart', component_property = 'hoverData'),   
    ]
)
def get_graph(status_, country_, territory_, city_, hbc_filter_, tm0_filter_, tm1_filter_, pc_filter_):
    
    
    #print(status_)
    #print(hbc_filter_)
    #print(tm0_filter_)

    ############ Drop Down Logic Field ##############
    #print(status_)
    #print(country_)
    #print(territory_)
    #print(city_)
    
    if status_ != None or country_ != None or  territory_ != None or city_ != None:
        df = mf.copy(deep = True)
        if status_ != None:
            df = df[df[drp_v1]==status_]
        if country_ != None:
            df = df[df[drp_v2]==country_]
        if territory_ != None:
            df = df[df[drp_v3]==territory_]
        if city_ != None:
            df = df[df[drp_v4]==city_]
    else:
        df = mf.copy(deep=True)
            
    
    ############ Hover Logic Field ##################
    if tm0_filter_ == None and hbc_filter_ == None and tm1_filter_ == None and pc_filter_ == None:
        #df = mf.copy(deep=True)
        pass

    elif type(tm0_filter_) == dict:
        tm0_filter_ = tm0_filter_['points'][0]['label']
        #print(tm0_filter_)
        city_ = tm0_filter_
        #df = mf.copy(deep=True)
        df = df[df[tm0_v]==tm0_filter_]

    elif type(hbc_filter_)==dict:
        hbc_filter_ = hbc_filter_['points'][0]['y']
        #df = mf.copy(deep=True)
        df = df[df[bar_v]==hbc_filter_]
    
    elif type(tm1_filter_)==dict:
        tm1_filter_ = tm1_filter_['points'][0]['label']
        #print(tm1_filter_)
        city_ = tm1_filter_
        #df = mf.copy(deep=True)
        df = df[df[tm1_v]==tm1_filter_]

    elif type(pc_filter_) == dict:
        pc_filter_ = pc_filter_['points'][0]['label']
        #print(pc_filter_)
        #df = mf.copy(deep=True)
        df = df[df[pc_v]==pc_filter_]
    
    Horizontal_BarChart = hbc(df)
    TreeMap0 = tmp0(df)
    TreeMap1= tmp1(df)
    PieChart = pic(df)
    Table0 = tab0(df)
    Table1 = tab1(df)

    
    #Horizontal_BarChart = hbc(status_)
    #TreeMap0 = tmp0(country_)
    #TreeMap1= tmp1(territory_)
    #PieChart = pic(city_)
    
    
    return[Horizontal_BarChart, TreeMap0, TreeMap1, PieChart, Table0, Table1]




# Server Loading Section
if __name__ == '__main__':
    app.run_server(port = 8090)
