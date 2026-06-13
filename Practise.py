from flask import Flask
app = Flask(__name__)

@app.route('/')

def home():
    return "Hello World"

# @app.route('/about')

# def about():
#     return "This is a about page"

# Dynamic route
@app.route('/about/<userName>')

def about(userName):
    return f'<h1>This is the about page of {userName}</h1>'


if __name__ == "__main__":
    app.run(debug=True)


    
