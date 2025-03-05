from flask import Flask
from flask_sqlalchemy import SQLAlchemy

    
# Always check which python we're executing.
# Make sure its not pointing to conda or Homebrew
# But a new virtual (poetry) environment that I've made

def create_app(config_overrides=None):
    app = Flask(__name__)
    # Part of Flask's feaute to aplabetically sort JSON keys.
    # JSON does not sort any keys
    # Command below is to stop it from alphabetically sorting.
    # app.json.sort_keys = False 

    # URI -> Uniform Resource Identifier
    # In production, this URI will define the credentials and 
    # Hostname of database server.
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.splite"
    if config_overrides:
        app.config.update(config_overrides)

    # Load the models
    from todo.models import db
    from todo.models.todo import Todo
    db.init_app(app)

    # Create data base variables
    with app.app_context():
        db.create_all()
        db.session.commit()
    
    # Register the blueprint
    from todo.views.routes import api
    app.register_blueprint(api)

    return app