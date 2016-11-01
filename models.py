from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker



Base = declarative_base()

### Many to many objects

class PersonGroup(Base):
    __tablename__ = 'person_group'
    person_id = Column(Integer, ForeignKey('_person.id'), primary_key=True)
    group_id = Column(Integer, ForeignKey('_group.id'), primary_key=True)

    group = relationship("Group", back_populates="persons")
    person = relationship("Person", back_populates="groups")

class Person(Base):
    __tablename__ = '_person'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    groups = relationship("PersonGroup", back_populates="person")

    emails = relationship("PersonEmail", back_populates="person")

    streets = relationship("PersonStreet", back_populates="person")

    phones = relationship("PersonPhone", back_populates="person")


    def __repr__(self):
        return "<Person(first_name='%s', last_name='%s')>" % ( self.first_name, self.last_name )

class Group(Base):
    __tablename__ = '_group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship("PersonGroup", back_populates="group")

    def __repr__(self):
        return "<Group(name='%s')>" % ( self.name )



class PersonEmail(Base):
    __tablename__ = 'person_email'
    person_id = Column(Integer, ForeignKey('_person.id'), primary_key=True)
    email_id = Column(Integer, ForeignKey('_email.id'), primary_key=True)

    email = relationship("Email", back_populates="persons")
    person = relationship("Person", back_populates="emails")


class Email(Base):
    __tablename__ = '_email'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship("PersonEmail", back_populates="email")

    def __repr__(self):
        return "<Email(name='%s')>" % ( self.name )





class PersonStreet(Base):
    __tablename__ = 'person_street'
    person_id = Column(Integer, ForeignKey('_person.id'), primary_key=True)
    street_id = Column(Integer, ForeignKey('_street.id'), primary_key=True)

    street = relationship("Street", back_populates="persons")
    person = relationship("Person", back_populates="streets")


class Street(Base):
    __tablename__ = '_street'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship("PersonStreet", back_populates="street")

    def __repr__(self):
        return "<Street(name='%s')>" % ( self.name )





class PersonPhone(Base):
    __tablename__ = 'person_phone'
    person_id = Column(Integer, ForeignKey('_person.id'), primary_key=True)
    phone_id = Column(Integer, ForeignKey('_phone.id'), primary_key=True)

    phone = relationship("Phone", back_populates="persons")
    person = relationship("Person", back_populates="phones")


class Phone(Base):
    __tablename__ = '_phone'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    persons = relationship("PersonPhone", back_populates="phone")

    def __repr__(self):
        return "<Phone(name='%s')>" % ( self.name )




# create database in RAM ( have to )

engine=create_engine('sqlite:///:memory:', echo=False)
# engine=create_engine('sqlite:///:memory:', echo=True)

Base.metadata.bind = engine

Base.metadata.create_all()

Session = sessionmaker(bind=engine)
db_session = Session()

