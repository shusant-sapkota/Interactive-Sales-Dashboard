import dash
from dash import dash_table
import plotly.express as px
import pandas as pd


# 4 Each Graph Functions  Section

#4.1 Horizontal Bar Chart
hbc_c1 = 'STATUS'
hbc_c2 = 'PRODUCTLINE'
hbc_c3 = 'SALES'
def hbc(df):
    #tm0_filter_ = tm0_filter_['points'][0]['label']
    #print(tm0_filter_)
    df_hbc = df[[hbc_c1,hbc_c2,hbc_c3]].groupby([hbc_c1, hbc_c2]).sum().reset_index()
    #df_hbc = df_hbc[df_hbc[hbc_c1] == status_]
    Horizontal_BarChart = px.bar(df_hbc, y = hbc_c2, x = hbc_c3, orientation='h', width=400, height=350, facet_row_spacing=0.04, facet_col_spacing=0.04)
    
    return Horizontal_BarChart

# 4.2 TreeMap 1

tmp0_c1 = 'COUNTRY'
tmp0_c2 = 'CITY'
tmp0_c3 = 'SALES'
def tmp0(df):
    #hbc_filter_ = hbc_filter_['points'][0]['y']
    #print(hbc_filter_)
    #df_t0 = df[df['PRODUCTLINE'] == hbc_filter_]
    df_t0 = df[[tmp0_c1, tmp0_c2, tmp0_c3]].groupby([tmp0_c1,tmp0_c2]).sum().sort_values(tmp0_c3, ascending=False).reset_index()
    #df_t0 = df_t0[df_t0[tmp0_c1]==country_]
    TreeMap0 = px.treemap(df_t0, names = tmp0_c2, values =tmp0_c3, parents = ['Cities of Countries']*len(df_t0), width=400, height=350)
    return TreeMap0


# 4.3 TreeMap 2
tmp1_c1 = 'TERRITORY'
tmp1_c2 = 'CITY'
tmp1_c3 = 'SALES'

def tmp1(df):
    #hbc_filter_ = hbc_filter_['points'][0]['y']
    #df_t1 = df[df['PRODUCTLINE']==hbc_filter_]
    df_t1 = df[[tmp1_c1, tmp1_c2, tmp1_c3]].groupby([tmp1_c1,tmp1_c2]).sum().sort_values(tmp1_c3, ascending=False).reset_index()
    #df_t1 = df_t1[df_t1[tmp1_c1]==territory_]
    TreeMap1 = px.treemap(df_t1, names =tmp1_c2, values =tmp1_c3, parents = ['Cities of Territories']*len(df_t1), width=400, height=350)

    return TreeMap1


# 4.4 PIE Chart
pic_c1 = 'CITY'
pic_c2 = 'DEALSIZE'
pic_c3 = 'SALES'
def pic(df):
    #hbc_filter_ = hbc_filter_['points'][0]['y']
    #df_pc = df[df['PRODUCTLINE']==hbc_filter_]
    df_pc = df[[pic_c1, pic_c2, pic_c3]].groupby([pic_c1, pic_c2]).sum().reset_index()
    #df_pc = df_pc[df_pc[pic_c1]==city_]
    PieChart = px.pie(df_pc, values = pic_c3, names = pic_c2,  width=350, height=350)
    return PieChart

tb00_c1 = 'CUSTOMERNAME'
tb00_c2 = 'SALES'

tb01_c1 = 'CUSTOMERNAME'
tb01_c2 = 'ORDERNUMBER'

def tab0(df):
    df_tb00 = df[[tb00_c1, tb00_c2]].groupby(tb00_c1).sum().reset_index()
    df_tb01 = df[[tb01_c1, tb01_c2]].groupby(tb01_c1).count().reset_index()
    df_tb0 = pd.merge(df_tb01, df_tb00 , on=tb00_c1)
    df_tb0[tb00_c2] = df_tb0[tb00_c2].round(2)
    #Table0 = ff.create_table(df_tb0[:8])
    Table0 = dash_table.DataTable(
                data=df_tb0.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_tb0.columns],
                page_action='none',
                fixed_rows = {'headers': True},
                filter_action = 'native',
                sort_action = 'native',
                style_header={
                    'fontSize': '14px',
                    'color': 'white',
                    'backgroundColor': 'black',
                    'fontWeight': 'bold'},
                style_cell = {
                    'fontSize': '12px',
                    'textAlign': 'center'
                },
                style_table={'height': '300px', 'width': '400px','overflowY': 'auto'})

    #print('Table0 returned')
    return Table0


tb10_lis = ['CUSTOMERNAME', 'COUNTRY', 'STATE', 'CITY', 'ADDRESSLINE1', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME']

tb11_c1 = 'CUSTOMERNAME'
tb11_c2 = 'SALES'

tb12_c1 = 'CUSTOMERNAME'
tb12_c2 = 'ORDERNUMBER'

def tab1(df):
    df_tb10 = df[tb10_lis].drop_duplicates()
    df_tb11 = df[[tb11_c1, tb11_c2]].groupby(tb11_c1).sum().reset_index()
    df_tb11[tb11_c2] = df_tb11[tb11_c2].round(2)
    
    df_tb12 = df[[tb12_c1, tb12_c2]].groupby(tb12_c1).count().reset_index()
    df_tb1 = pd.merge(df_tb10,pd.merge(df_tb12,df_tb11,on=tb12_c1), on=tb12_c1)
    #Table1 = ff.create_table(df_tb1[:8])
    Table1 = dash_table.DataTable(
                data=df_tb1.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_tb1.columns],
                page_action='none',
                fixed_rows = {'headers': True},
                filter_action = 'native',
                sort_action = 'native',
                style_header={
                    'fontSize': '14px',
                    'color': 'white',
                    'backgroundColor': 'black',
                    'fontWeight': 'bold'},
                style_cell = {
                    'fontSize': '12px',
                    'textAlign': 'center'
                },
                style_table={'height': '300px', 'width': '900px', 'overflowY': 'auto'})

    #print('Table1 returned')
    return Table1