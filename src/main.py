import os
from flask import Flask
from flask_migrate import Migrate
from api.models import db
from api.routes import api

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder (official Docs)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#Define environment
ENV = os.getenv("FLASK_ENV")

# database configuration
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"

#to avoid warning message
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



MIGRATE = Migrate(app, db, compare_type = True)

# initialize the app with the extension
db.init_app(app)

# Add all endpoints form the API with a "api" prefix
app.register_blueprint(api, url_prefix='/api')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))