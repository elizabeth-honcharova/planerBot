
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,Date, BOOLEAN, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "User"

    user_id = Column(Integer, primary_key=True)
    e_mail = Column(String(250), nullable=False)


class List_db(Base):
    __tablename__ = 'List'

    list_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.user_id"))
    title = Column(String(250), nullable=False)

class Task(Base):
    __tablename__ = 'Task'

    task_id = Column(Integer, primary_key=True)
    list_id = Column(Integer, ForeignKey("List.list_id"))
    title = Column(String(250))
    description = Column(String(250))
    complation_date = Column(Date)
    complation_time = Column(Time)
    iscomplete = Column(BOOLEAN, default=False)


Base.metadata.create_all(engine)