from flask import Flask
from .models import db
from flask_login import LoginManager
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes.auth import auth
    from .routes.main import main
    from .routes.blog import blog
    from .routes.profile import profile

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(blog)
    app.register_blueprint(profile)

    return app