from models import db_session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy import or_
from sqlalchemy import and_
from sqlalchemy import not_


from models import Person, Group, PersonGroup
from models import Email, PersonEmail
from models import Street, PersonStreet
from models import Phone, PersonPhone



class BookManager(object):
    """
    """
    def __init__(self):
        # get the db session
        self.session = db_session

    def createPerson(self, first_name, last_name):
        a = Person(first_name=first_name, last_name=last_name)
        self.session.add(a)
        self.session.commit()
        return a

    def createGroup(self, name):
        a = Group(name=name)
        self.session.add(a)
        self.session.commit()
        return a

    def createEmail(self, name):
        a = Email(name=name)
        self.session.add(a)
        self.session.commit()
        return a
    
    def createStreet(self, name):
        a = Street(name=name)
        self.session.add(a)
        self.session.commit()
        return a
    
    def createPhone(self, name):
        a = Phone(name=name)
        self.session.add(a)
        self.session.commit()
        return a

    ##### add-ons

    # Add a group to a person
    def addGroupToPerson(self, person, group):
        # do
        try:
            person_group = PersonGroup(person=person, group=group)
            self.session.add(person_group)
            self.session.commit()
        except Exception, e:
            return False
        return True

    # Add an email to a person
    def addEmailToPerson(self, person, email):
        # do
        try:
            # 1) try create an email object if there is no
            person_email = PersonEmail(person=person, email=email)

            self.session.add(person_email)

            self.session.commit()
        except Exception, e:
            return False
        return True


    # Return a list of person instances filtered by name
    def getPersonByName(self, name):
        if (name.__contains__(" ")):
            first = name.split(" ")[0]
            last = name.split(" ")[1]

            objs = self.session.query(Person).filter(or_(Person.first_name == first , Person.last_name == last))
            return objs.all()
        else:
            objs = self.session.query(Person).filter(or_(Person.first_name == name , Person.last_name == name))
            return objs.all()


    # Return a list of person instances filtered by email
    def getPersonByEmail(self, email):
        # return Person.get_person_by_email(email) 
        # 1). find the email: we use "like" in SQL
        the_email = self.session.query(Email).filter(Email.name.like(email+"%")).all()
        if len(the_email) == 0:
            return 0
        # we only the the one most alike
        else:
            the_email = the_email[0]
        # 2). find persons who have this email
        return self.session.query(Person).join(PersonEmail).filter(Email.id == the_email.id).all()

    # Return a list of person instances filtered by group
    def getGroupMembers(self, group):
        # return Person.get_person_by_email(email) 
        # 1.) search to the group
        the_group = self.session.query(Group).filter(Group.name == group).all()
        if len(the_group) == 0:
            return []
        # select the choosen group
        else:
            the_group = the_group[0]
        # 2.) join the table , find person
        return self.session.query(Person).join(PersonGroup).filter(and_(PersonGroup.person_id == Person.id , PersonGroup.group_id == the_group.id )).all()

        # return self.session.query(Group.persons).all()
        # return self.session.query(Person).join(Group).filter(Group.name == group).all()

    # Return a list of group instances filtered by person
    def getGroupsByPerson(self, person_name):
        # return Person.get_person_by_email(email) 
        # 1). find the person
        the_person = self.getPersonByName(person_name)
        if len(the_person) == 0:
            return []
        # only return the first match
        else:
            the_person = the_person[0]
        # 2). find the groups the person belongs to

        return self.session.query(Group).join(PersonGroup.person).filter(Person.id == the_person.id).all()


    


if __name__ == "__main__":
    session = db_session
    
    DEBUG = True


    if DEBUG:
        p = Parent()
        c = Child()
        a = Association(extra_data='some data')
        a.child = Child()
        p.children.append(a)

        for assoc in p.children:
            print(assoc.extra_data)
            print(assoc.child)

    
    # create objects
    person1 = Person(first_name='Alex', last_name='Hulk')
    person2 = Person(first_name='Lily', last_name='White')
    person3 = Person(first_name='Tom', last_name='Green')

    group1 = Group(name='Linux')    
    group2 = Group(name='Windows')    
    group3 = Group(name='MacOS')    

    # email1 = Email(name='firstme1@go.com')
    # email2 = Email(name='email2@wo.com')
    # email3 = Email(name='email3@ko.com')

    # street1 = Street(name='St. 111, LA')
    # street2 = Street(name='Nice Town, New York')

    # phone1 = Phone(name='12312312312')
    # phone2 = Phone(name='89234908124')

    # save objects
    session.add(person1)
    session.add(person2)
    session.add(person3)

    session.add(group1)
    session.add(group2)
    session.add(group3)

    # session.add(email1)
    # session.add(email2)
    # session.add(email3)

    # session.add(street1)
    # session.add(street2)

    # session.add(phone1)
    # session.add(phone2)

    # commit session
    session.commit()

    person_group1 = PersonGroup(group=group1)

    # person_group1.group = group1

    person1.groups.append(person_group1)

    # person1.groups.append(group1)
    # person1.groups.append(group2)
    # person1.groups.append(group3)

    # person2.groups.append(group1)

    # person2.emails.append(email3)

    session.commit()

    # gotten = session.query(Person.first_name).filter(first_name=='Alex')
    gotten = session.query(Person.first_name == 'Alex')

    # print(gotten)
    all_ =  session.query(Person).all()
    # print(all_)


    # find who joined group Linux
    persons = session.query(Person).join(Person.groups).filter(Group.name == 'Linux')


    for p in persons:
        print(p)


