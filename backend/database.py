from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://appdev_todolist_fastapi_db_user:gwFcEye7sx2P6fzuKurqd3FBpq3ZFEzs@dpg-cvv7989r0fns73a6398g-a/appdev_todolist_fastapi_db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
