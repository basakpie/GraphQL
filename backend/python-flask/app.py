# Imports
from flask import Flask

# app initialization
app = Flask(__name__)

@app.route('/')
def index():
    return '<p> Hello World</p>'

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)