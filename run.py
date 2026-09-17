# ================================
# run.py - ENTRY POINT
# This is the first file you run
# It starts your website
# ================================

from app import create_app, db  # Importing the app creator and database

app = create_app()  # Creating the website using our create_app() function from app/__init__.py

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This creates all database tables automatically
                         # based on the models we defined in models.py

    app.run(debug=True)  # This starts the website at http://127.0.0.1:5000
                         # debug=True shows detailed errors while we are building