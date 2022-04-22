from flask import Flask, request, render_template, session, redirect 

from data_processing import get_data

import plotly.express as px
import os

app = Flask(__name__)

df = get_data()

fig = px.line(df,
        x = 'Date',
        y = 'WSR0')

fig.write_html('static/plotly_graph.html')

# @app.route('/', methods=("POST", "GET"))
# def html_table():

#     return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/')

def home():
  return render_template('main.html')

if __name__ == '__main__':

  app.run(debug = True, host = '0.0.0.0')

