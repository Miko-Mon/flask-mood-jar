from heartscape import create_app, db
from heartscape import models

app = create_app()

with app.app_context():
    db.create_all()
    print("Created tables")