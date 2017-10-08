from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql import select

class orm(object):
    """description of class"""

BD = declarative_base()

class User(BD):
    __tablename__ = "User"
    userName = Column('userName', String, primary_key=True)
    descUser = Column('descUser', String)
    Communities = Column('Communities', String)

class Answer(BD):
    __tablename__ = "Answer"
    id = Column('id', Integer, primary_key=True)
    idPregunta = Column('idPregunta',Integer)
    Respuesta = Column('Respuesta', String)
    fecha = Column('descRespu', String)
    userNameRespuesta = Column('userNameRespuesta', String, ForeignKey("User.userName"), nullable=False)

class Question(BD):
    __tablename__ = "Question"
    id = Column('id', Integer, primary_key=True)
    Pregunta = Column('Pregunta', String)
    descPregun = Column('descPregun', String)
    userNamePregunta = Column('userNamePregunta', String, ForeignKey("User.userName"), nullable=False)




engine = create_engine('sqlite:///ComunidadStack.db', echo=True)
#engine = create_engine('sqlite:///Stack.db', echo=True)

BD.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
