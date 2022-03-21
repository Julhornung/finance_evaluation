from flask import Flask, request, render_template, session, redirect 

from data_processing import get_data

app = Flask(__name__)

# df = get_data()

# print(df.head())



# @app.route('/', methods=("POST", "GET"))
# def html_table():

#     return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)


@app.route('/')
def hello_world():
      
  return render_template('main.html')
  # return 'Hello Docker!\n'

if __name__ == '__main__':

  app.run(debug = True, host = '0.0.0.0')

