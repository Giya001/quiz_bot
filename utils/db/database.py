from sqlalchemy import create_engine, Column, Integer, String, BigInteger
from sqlalchemy.orm import declarative_base, sessionmaker
from data.config import PG_DB,PG_HOST,PG_PASS,PG_USER,PG_PORT

engine = create_engine(f'postgres + psycopg2://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}')

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True,autoincrement=True)
    chat_id=Column(BigInteger,unique=True)
    name=Column(String(50),nullable=False)
    phone=Column(String(12))
