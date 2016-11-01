class Person(object):
    """
    Person:
    """
    first_name=""
    last_name=""
    email_address=set()
    phone_number=set()
    group=set()


    def __init__(self):
        super(Group, self).__init__()


    def __init__(self):
        pass

class Group(object):
    """Doc string for Group"""
    # person=Person()
    person=set()

    def __init__(self):
        """
        ::    @todo
        """
        super(Group, self).__init__()


class AddressBook(object):
    """Doc string for AddressBook"""
    group = Group()
    addressbook = []
    __default_group = "generic"

    def __init__(self):
        """
        ::    @todo
        """
        super(AddressBook, self).__init__()

    def add_person_to_group(self, person=None, group=None):
        if person is None:
            raise ValueError("person not declared") 
        if group is None:
            group = self.__default_group


class BookManager(object):
    """Doc string for BookManager"""
    persons = set()
    groups = set()
    addressbook = AddressBook()         # assuming we only have 1 book
    __default_group = "default"
    matrix = [[[]]]

    def __init__(self):
        """
        ::    @todo
        """
        super(BookManager, self).__init__()
        # lets add one default group for all people
        self.groups.add(self.__default_group)
    

    def add_person_to_group(self, person=None, group=None):
        if person is None:
            raise ValueError("person not declared") 
        elif person is not Person():
            raise ValueError("person should be a Person() instance")
        if group is None:
            group = self.__default_group
