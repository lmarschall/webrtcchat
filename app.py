# from flask import Flask
# from flask import render_template
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# # run the application
# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__, static_folder = "app/dist/", template_folder = "app/dist")

@app.route('/')
def index():
    return render_template("index.html")