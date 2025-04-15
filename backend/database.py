from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual PostgreSQL connection string
DATABASE_URL = "postgresql://username:password@localhost/dbname"

# Create the SQLAlchemy engine and session local
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Initialize the database tables
def init_db():
    Base.metadata.create_all(bind=engine)
