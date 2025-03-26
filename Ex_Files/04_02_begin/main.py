from flask import Flask

app = Flask(__name__) #dunderscore 

@app.route("/")
def hello():
  return "Hello world"

app.run(debug=True)
