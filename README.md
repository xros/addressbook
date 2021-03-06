Address Book
=============
By [Alexander Liu](https://github.com/xros)

This is an address book module written in Python.

It is designed to be extensive as a module. Runs in RAM, very efficent. 

**Core concept** --> Many to Many Database Relationship.

Objectives: To solve real-world people in different groups or books on different shelfs and such.


### Usage
Preparation for the environment
```
pip install -r requirments.txt
```

### Coding example
```python
from bookmanager import BookManager

bm = BookManager()
someone = bm.createPerson(first_name='Richard', last_name='Stallman')
gnu_group = bm.createGroup('GNU')

flag=bm.addGroupToPerson(someone, gnu_group)

if flag:
    print("Welcome to GNU group!!!")
else:
    print("Sad and pitty...")

members = bm.getGroupMembers("GNU")

for m in members:
    print(m.first_name)
```

##### What can it do?

Example of facts:

- A person has a first name and a last name.
- A person has one or more street addresses.
- A person has one or more email addresses.
- A person has one or more phone numbers.
- A person can be a member of one or more groups.
- An address book is a collection of persons and groups.

Example of required features:

- Add a person to the address book.
- Add a group to the address book.
- Given a group we want to easily find its members.
- Given a person we want to easily find the groups the person belongs to.
- Find person by name (can supply either first name, last name, or both).
- Find person by email address (can supply either the exact string or a prefix string, ie. both "alexander@company.com" and "alex" should work).


### API structure
```
class BookManager(__builtin__.object)
 |  Methods defined here:
 |
 |  __init__(self)
 |
 |  addEmailToPerson(self, person, email)
 |      # Add an email to a person
 |
 |  addGroupToPerson(self, person, group)
 |      # Add a group to a person
 |
 |  createEmail(self, name)
 |
 |  createGroup(self, name)
 |
 |  createPerson(self, first_name, last_name)
 |
 |  createPhone(self, name)
 |
 |  createStreet(self, name)
 |
 |  getGroupMembers(self, group)
 |      # Return a list of person instances filtered by group
 |
 |  getGroupsByPerson(self, person_name)
 |      # Return a list of group instances filtered by person
 |
 |  getPersonByEmail(self, email)
 |      # Return a list of person instances filtered by email
 |
 |  getPersonByName(self, name)
 |      # Return a list of person instances filtered by name
 ```

 This module is built on top of SQLAlchemy and sqlite3, running in RAM, and it will return native SQLAlchemy instances. 

 
#### API table


| Functionality | Method | Input Parameters | returned type | 
| ------------ | ---- | ---------------- | ------------|
| Create a person object | createPerson() | [string] first_name, [string] last_name | A SQLAlchemy model instance |
| Create a group object | createGroup() | [string] name | A SQLAlchemy model instance |
| Create a email object | createEmail() | [string] name | A SQLAlchemy model instance |
| Create a street object | createStreet() | [string] name | A SQLAlchemy model instance |
| Create a phone object | createPhone() | [string] name | A SQLAlchemy model instance |
| Add an Email address to a person | addEmailToPerson() | [sqla model instance] person, [sqla model instance] email | boolean |
| Add an group to a person | addGroupToPerson() | [sqla model instance] person, [sqla model instance] group | boolean |
| Get all members from a group | getGroupMembers() | [string] group | A list of SQLAlchemy model instances |
| Get groups belongs to a person | getGroupsByPerson() | [string] person_name | A list of SQLAlchemy model instances |
| Get persons by a Email | getPersonByEmail() | [string] email | A list of SQLAlchemy model instances |
| Get persons by a person name or only prefix | getPersonByName() | [string] name | A list of SQLAlchemy model instances |


 

### Run the test script

```
python run_test.py
```

![image test](https://github.com/xros/addressbook/blob/master/static/snapshot355.png?raw=true)

### Learn why it is in this way

[See .test](https://github.com/xros/addressbook/tree/master/.test)
