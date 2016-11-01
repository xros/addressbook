Address Book
=============

This is an address book module written in Python.

It is designed to be extensive


### Usage
Preparation for the environment
```
pip install -r requirments.txt
```

### Coding example
```python
from bookmanager import BookManager

bm = BookManager()
someone = bm.createPerson('Richard', 'Stallman')
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

 This module is built on SQLAlchemy, and it will return native SQLAlchemy instances. 
 
 For example,


 | Functionality | Method | Input Parameters | returned type | 
 | ------------ | :----: | :----------------: | ------------:|
 | Create a person object | createPerson() |  first_name,  last_name | A SQLAlchemy model instance |



 
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
