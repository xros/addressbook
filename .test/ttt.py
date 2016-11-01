import sqlite3
from sql_models import *

class BookManager(object):
    """Doc string for BookManager"""

    def __init__(self):
        """
        ::    @todo
        """
        super(BookManager, self).__init__()
        self.db = self.init_relation()

    def init_relation(self):
        """
        """
        conn = sqlite3.connect(':memory:')
        
        c = conn.cursor()
        
        
        # create all havings
        c.execute(sql_create_addressbook)
        c.execute(sql_create_group)
        c.execute(sql_create_street)
        c.execute(sql_create_email) 
        c.execute(sql_create_phone) 

        # create person
        c.execute(sql_create_person)
        
        # create mappings
        c.execute(sql_create_person_group)
        c.execute(sql_create_person_street)
        c.execute(sql_create_person_email)
        c.execute(sql_create_person_phone)

        return c
    
            
    def createPerson(self, first_name=None, last_name=None):
        query = "INSERT INTO ad_person (first_name, last_name) VALUES ('%s', '%s');" \
            % (first_name, last_name)
        self.db.execute(query)
        # return an object named lastid
        last_id = self.db.lastrowid
        # return an object

    def createPerson(self, first_name=None, last_name=None):
        query = "INSERT INTO ad_person (first_name, last_name) VALUES ('%s', '%s');" \
            % (first_name, last_name)
        self.db.execute(query)

    def createGroup(self, name=None):
        query = "INSERT INTO ad_group (name ) VALUES ('%s');" \
            % (name)
        self.db.execute(query)
    
    def createStreet(self, name=None):
        query = "INSERT INTO ad_street (name ) VALUES ('%s');" \
            % (name)
        self.db.execute(query)
    
    def createEmail(self, name=None):
        query = "INSERT INTO ad_email (name ) VALUES ('%s');" \
            % (name)
        self.db.execute(query)
    
    def createPhone(self, name=None):
        query = "INSERT INTO ad_phone (name ) VALUES ('%s');" \
            % (name)
        self.db.execute(query)
    
    def showPerson(self):
        query = "SELECT * from ad_person;"
        for row in self.db.execute(query):
            print(row)

    ######
    ### Many to many objects
    ######

    def createPersonGroup(self, person_id=None, group_id=None):
        query = "INSERT INTO ad_person_group (person_id, group_id) VALUES ('%d', '%d');" \
            % (person_id, group_id)
        self.db.execute(query)

    def createPersonStreet(self, person_id=None, street_id=None):
        query = "INSERT INTO ad_person_street (person_id, street_id) VALUES ('%d', '%d');" \
            % (person_id, street_id)
        self.db.execute(query)

    def createPersonEmail(self, person_id=None, email_id=None):
        query = "INSERT INTO ad_person_email (person_id, email_id) VALUES ('%d', '%d');" \
            % (person_id, email_id)
        self.db.execute(query)

    def createPersonPhone(self, person_id=None, phone_id=None):
        query = "INSERT INTO ad_person_phone (person_id, phone_id) VALUES ('%d', '%d');" \
            % (person_id, phone_id)
        self.db.execute(query)

    def showPersonGroup(self):
        query = "SELECT * from ad_person_group;"
        for row in self.db.execute(query):
            print(row)


    def showGroupByPerson(self, person_id=None):
        # TODO
        query = """SELECT name FROM ad_group JOIN ad_person_group ON ad_person_group.person_id='%s' \
                ;
                """
        # query = "SELECT group_id from ad_person_group where person_id='%d';" \
            # % person_id
        for row in self.db.execute(query):
            print(row)
            # query_2 = "SELECT name FROM ad_group WHERE id='%d';" \
                # % row
            # for r in self.db.execute(query_2):
                # print(r)



    

if __name__ == "__main__":
    pass
