from website import create_app, db
from website import models

app = create_app()

with app.app_context():
    db.create_all()
    print("Created tables")