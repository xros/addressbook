Address Book
=============

This is an address book module written in Python.

It is designed to be extensive


### Usage
Prepare for the environment
```
pip install -r requirments.txt
```

### Coding example
```
from bookmanager import BookManager

bm = BookManager()
someone = bm.createPerson('Richard', 'Stallman')
gnu_group = bm.createGroup('GNU')

flag=bm.addGroupToPerson(someone, gnu_group)

if flag:
    print("Welcome to GNU group!!!")
else:
    print("Sad and pitty...")

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

### Run the test script

```
python run_test.py
```

![image test](https://github.com/xros/addressbook/blob/master/static/snapshot355.png?raw=true)
