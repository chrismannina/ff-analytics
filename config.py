import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')  # SQLite for local development
# SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'  # Uncomment for PostgreSQL deployment

SQLALCHEMY_TRACK_MODIFICATIONS = False
