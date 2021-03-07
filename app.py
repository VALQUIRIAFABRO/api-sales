from flask import Flask
import importlib.util


app = Flask(__name__)
mdl = importlib.import_module('module.modules')
mdl.make_rout(app)

if __name__ == '__main__':
    app.run(debug=True)