from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
# This is the entry point for the Flask application