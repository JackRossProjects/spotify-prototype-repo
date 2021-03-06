import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd
import pickle
import re

df = pd.read_csv('song_data.csv')

########### Initiate the app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
app.title='Spotifind'

########### Set up the layout
app.layout = html.Div(children=[
    html.H1('Find music that fits you!'),
    html.Div([
        html.H6('Danceability'),
        dcc.Slider(
            id='slider-1',
            min=0,
            max=1,
            step=0.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.Br(),
        html.H6('Energy'),
        dcc.Slider(
            id='slider-2',
            min=0,
            max=1,
            step=0.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.H6('Key'),
        dcc.Slider(
            id='slider-3',
            min=0,
            max=11,
            step=1,
            marks={i:str(i) for i in range(0,12)},
            value=0,
        ),
        html.Br(),
        html.H6('Loudness'),
        dcc.Slider(
            id='slider-4',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.H6('Mode'),
        dcc.Slider(
            id='slider-5',
            min=0,
            max=1,
            step=1,
            marks={i:str(i) for i in [0,1]},
            value=0,
        ),
        html.Br(),
        html.H6('Speechiness'),
        dcc.Slider(
            id='slider-6',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.H6('Acousticness'),
        dcc.Slider(
            id='slider-7',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.Br(),
        html.H6('Instrumentalness'),
        dcc.Slider(
            id='slider-8',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.H6('Liveness'),
        dcc.Slider(
            id='slider-9',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.Br(),
        html.H6('Valence'),
        dcc.Slider(
            id='slider-10',
            min=0,
            max=1,
            step=.1,
            marks={i:str(i) for i in [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]},
            value=0,
        ),
        html.H6('Tempo'),
        dcc.Slider(
            id='slider-11',
            min=0,
            max=200,
            step=25,
            marks={i:str(i) for i in [0,25,50,75,100,125,150,175,200]},
            value=0,
        ),
        html.Br(),
        html.H6('Duration (mins)'),
        dcc.Slider(
            id='slider-12',
            min=0,
            max=300000,
            step=60000,
            marks={i:str(i) for i in [1,2,3,4,5]},
            value=0,
        ),
        html.H6('Time Signature'),
        dcc.Slider(
            id='slider-13',
            min=0,
            max=2,
            step=1,
            marks={i:str(i) for i in [0,1,2]},
            value=0,
        ),
        html.Br(),
        html.H6('Popularity'),
        dcc.Slider(
            id='slider-14',
            min=0,
            max=100,
            step=10,
            marks={i:str(i) for i in [0,10,20,30,40,50,60,70,80,90,100]},
            value=0,
        ),

        html.H6(id='output-message', children='output will go here'),
    
    
    
    ]),
    html.Br(),
])



################ Interactive callbacks
@app.callback(Output('output-message', 'children'),
            [
            Input('slider-1', 'value'),
            Input('slider-2', 'value'),
            Input('slider-3', 'value'),
            Input('slider-4', 'value'),
            Input('slider-5', 'value'),
            Input('slider-6', 'value'),
            Input('slider-7', 'value'),
            Input('slider-8', 'value'),
            Input('slider-9', 'value'),
            Input('slider-10', 'value'),
            Input('slider-11', 'value'),
            Input('slider-12', 'value'),
            Input('slider-13', 'value'),
            Input('slider-14', 'value')
            ])

def display_results(value0, value1, value2, value3, value4, value5, value6, value7,
            value8, value9, value10, value11, value12, value13):
    file = open('spotify_model_k5.pkl', 'rb')
    model = pickle.load(file)
    file.close()
    new_obs=[[value0, value1, value2, value3, value4, value5, value6, value7,
            value8, value9, value10, value11, value12, value13]]
    pred = model.predict(new_obs)[0]
    return 'You might like the song "' + f'{pred}' + '" !'


############ Execute the app
if __name__ == '__main__':
    app.run_server()
