from ttt import BookManager

"""
Test case
"""


if __name__ == "__main__":
    a = BookManager()

    # create person
    a.createPerson(first_name='Alex', last_name='Joon')         # id 1
    a.createPerson(first_name='Tom', last_name='Green')         # id 2
    print("#### show all person ####")
    a.showPerson()

    # create group
    a.createGroup(name='cosplay')                               # id 1
    a.createGroup(name='Vim')                                   # id 2
    a.createGroup(name='music')                                 # id 3

    
    # create street
    a.createStreet(name='St. 11 New York')                      # id 1
    a.createStreet(name='St. 12 L.A.')                          # id 2

    # create email
    a.createEmail(name='someone@somewhere.com')                 # id 1
    a.createEmail(name='someone223@somewhere.com')              # id 2
    a.createEmail(name='lily@aol.com')                          # id 3
    a.createEmail(name='alexander@company.com')                 # id 4

    # create phone
    a.createPhone(name='2312344')                               # id 1
    a.createPhone(name='5934244')                               # id 2
    a.createPhone(name='9091003')                               # id 3


    # create relationship -- Many To Many
    a.createPersonGroup(person_id=1, group_id=1)
    a.createPersonGroup(person_id=2, group_id=1)
    a.createPersonGroup(person_id=2, group_id=3)

    a.createPersonStreet(person_id=1, street_id=1)
    a.createPersonStreet(person_id=1, street_id=2)

    a.createPersonEmail(person_id=1, email_id=1)
    a.createPersonEmail(person_id=1, email_id=4)
    a.createPersonEmail(person_id=2, email_id=1)
    a.createPersonEmail(person_id=2, email_id=3)

    a.createPersonPhone(person_id=1, phone_id=2)

    # show person group
    print("#### show all person group ####")
    a.showPersonGroup()

    # show group by person
    print("#### show group by person id: 1 ####")
    a.showGroupByPerson(person_id=1)

    print("#### show group by person id: 2 ####")
    a.showGroupByPerson(person_id=2)

