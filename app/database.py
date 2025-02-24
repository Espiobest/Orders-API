from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import psycopg2
import os
import dotenv
from .models import Base

dotenv.load_dotenv('.env')
DB_URL = os.environ.get("DB_URL", "sqlite:///./trades.db")


def ensure_database_exists():
    """Check if the database exists, and create it if it doesn't."""
    try:
        default_db_url = DB_URL.replace("/trades", "/postgres")  # Connect to default 'postgres' DB
        conn = psycopg2.connect(default_db_url)
        conn.autocommit = True
        cur = conn.cursor()

        # Check if the 'trades' database exists
        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'trades'")
        exists = cur.fetchone()

        if not exists:
            print("Database 'trades' does not exist. Creating...")
            cur.execute("CREATE DATABASE trades;")
            print("Database 'trades' created successfully.")

        cur.close()
        conn.close()
    except Exception as e:
        global engine
        engine = create_engine("sqlite:///./trades.db", echo=True)


def init_db():
    engine = create_engine(DB_URL, echo=True)
    ensure_database_exists()
    Base.metadata.create_all(bind=engine)


def get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
