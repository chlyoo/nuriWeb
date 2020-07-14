from flask import Flask
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()

def create_app():
	app = Flask(__name__) # modified 20191108
	bootstrap.init_app(app)
    # attach routs and custom error pages here
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	return app