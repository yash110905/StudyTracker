from flask import Flask
from database import db
from flask_login import LoginManager
from models import User
from routes.auth import auth

app =Flask(__name__)
app.config["SECRET_KEY"] = "study-tracker-secret"

#database config 
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///study_tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #database initialization

#login manager
login_manager = LoginManager()
login_manager.init_app(app)

#Redirect unauthorized users
login_manager.login_view = "auth.login"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route("/")
def home():
    return"Study tracker is running!!!"

with app.app_context():
    db.create_all() #will create tables in database 
app.register_blueprint(auth)    
if __name__ == "__main__":
    app.run(debug=True)