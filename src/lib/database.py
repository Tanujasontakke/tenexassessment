from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
DATABASE_URL= "sqlite:///./todos.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,bind=False)
Base = declarative_base()