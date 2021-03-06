from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

Base = declarative_base()


class Question1(Base):
    __tablename__ = 'Question'
    id = Column(Integer, primary_key=True)
    rt = Column(String)


class PotentialAnswer(Base):
    __tablename__ = 'Potential_Answers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    name1 = Column(String)
    name2 = Column(String)
    name3 = Column(String)
    Question_id = Column(Integer, ForeignKey('Question.id'))
    potentialanswer = relationship(Question1, backref=backref('potential_answer', uselist=True))


class ActualAnswer(Base):
    __tablename__ = 'Answers'
    id = Column(Integer, primary_key=True)
    qid = Column(Integer)
    answer = Column(Integer)
    answer1 = Column(Integer)
    answer2 = Column(Integer)
    answer3 = Column(Integer)
    Potential_Answers_id = Column(Integer, ForeignKey('Potential_Answers.id'))
    actualanswer = relationship(PotentialAnswer, backref=backref('actual_answer', uselist=True))
    
