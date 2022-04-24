from flask import Flask, request, render_template, session, redirect 

from data_processing import get_data

import plotly.express as px
import plotly
import os
import json

app = Flask(__name__)

df = get_data()

# fig = px.line(df,
#         x = 'Date',
#         y = 'WSR0')

# fig.write_html('static/plotly_graph.html')

def plotly_global_timeseries(df):

  fig = px.line(df,
          x = 'Date',
          y = 'WSR0')

  # fig = fig.update_xaxes(rangeslider_visible=True)

  fig.update_layout(width=1000, height=500)

  plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

  return (plot_json)

# @app.route('/', methods=("POST", "GET"))
# def html_table():

#     return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/')

def home():
      
  plot_json = plotly_global_timeseries(df)

  return render_template('home.html', plot_json = plot_json)

if __name__ == '__main__':

  app.run(debug = True, host = '0.0.0.0')

