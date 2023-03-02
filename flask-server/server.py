from flask import Flask

app = Flask(__name__)

#Members API route
@app.route('/members')
def member():
    return {"members":["m1","m2"]}
 

if __name__ == '__main__':
    app.run(debug=True)