from flask import Flask
from data_processing import get_data

df = get_data()

print(df.head())

app = Flask(__name__)

@app.route('/')

def hello_world(df):

  return(df.head())

  # return 'Hello Docker!\n'

if __name__ == '__main__':

  app.run(debug = True, host = '0.0.0.0')

