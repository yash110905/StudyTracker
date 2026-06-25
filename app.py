from flask import Flask
from database import db
app =Flask(__name__)


#database config 
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///study_tracker.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app) #database initialization

@app.route("/")
def home():
    return"Study tracker is running!!!"

with app.app_context():
    db.create_all() #will create tables in database 
    
if __name__ == "__main__":
    app.run(debug=True)