from website import create_app, db

app = create_app()

with app.app_context():
    try:
        with db.engine.connect() as conn:
            result = conn.execute(db.text("SELECT DATABASE()"))
            print("Connected to database:", result.scalar())

    except Exception as e:
        print("Error connecting to database: ", e)