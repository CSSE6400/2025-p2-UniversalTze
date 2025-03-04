from flask import Flask
from flask_sqlalchemy import SQLAlchemy

    """Always check which python we're executing.
    Make sure its not pointing to conda or Homebrew
    But a new virtual (poetry) environment that I've made
    """
def create_app():
    app = Flask(__name__)
    # URI -> Uniform Resource Identifier
    # In production, this URI will define the credentials and 
    # Hostname of database server.
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.splite"
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