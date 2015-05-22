import flask
import flask.ext.restless

from config import config
import os


def create_app(config_name, database_engine):
    """
    Generate app based on Flask instance.

    :type config_name: string
    :param config_name: Config Type (i.e. development, staging, production).

    :rtype: Object
    :return: Flask Object.
    """
    app = flask.Flask(__name__)

    # Load generic configs.
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Save environment type
    app.config['ENVIRONMENT'] = config_name

    # Init database from environment variable.
    databases_conf = app.config['GENERAL']['databases']
    app.config['SQLALCHEMY_DATABASE_URI'] = databases_conf[database_engine]

    from api_0_1.models.model import db
    db.init_app(app)
    db.app = app

    # Import model classes.
    from api_0_1.models.user import User
    from api_0_1.models.role import Role

    # Create db if not exist (defined at above models).
    db.create_all()

    # Import views clasess.
    from api_0_1.controllers.users import Users
    from api_0_1.controllers.roles import Roles

    Users = Users()
    Roles = Roles()

    # Create the Flask-Restless API manager.
    manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

    # Create API endpoints.
    manager.create_api(
        User,
        url_prefix=Users.url_prefix,
        methods=Users.methods,
        include_columns=Users.include_columns,
        exclude_columns=Users.exclude_columns,
        preprocessors=Users.preprocessors,
        postprocessors=Users.postprocessors
    )

    manager.create_api(
        Role,
        url_prefix=Roles.url_prefix,
        methods=Roles.methods,
        include_columns=Roles.include_columns,
        exclude_columns=Roles.exclude_columns,
        preprocessors=Roles.preprocessors,
        postprocessors=Roles.postprocessors
    )

    return app


try:
    if os.environ['ENV']:
        environment = os.environ['ENV']
except KeyError, e:
    environment = 'development'

try:
    if os.environ['DATABASE']:
        database = os.environ['DATABASE']
except KeyError, e:
    database = 'sqlite3'

app = create_app(environment, database)
