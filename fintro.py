from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask is micro level framework  .  Flask is a fun and easy framework'
