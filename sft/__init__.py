from flask import Flask
from flask_session import Session
import os

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "sft.sqlite"),
        SESSION_TYPE="filesystem",
    )
    sess = Session()
    sess.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Load database commands
    from . import db
    db.init_app(app)

    # Load information page blueprint
    from . import info
    app.register_blueprint(info.bp)

    # Load admin panel blueprint
    from . import admin
    app.register_blueprint(admin.bp)

    # Load authentication blueprint
    from . import auth
    app.register_blueprint(auth.bp)

    return app
