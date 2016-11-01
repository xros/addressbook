sql_create_addressbook = """
CREATE TABLE ad_book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
"""

sql_create_person = """
CREATE TABLE ad_person (
    id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT,
    last_name TEXT
    );
"""

sql_create_group = """
CREATE TABLE ad_group(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
"""

sql_create_email = """
CREATE TABLE ad_email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    );
"""

sql_create_street = """
CREATE TABLE ad_street (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    );
"""

sql_create_phone = """
CREATE TABLE ad_phone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
    );
"""

### Many-to-many mappings
sql_create_person_group = """
CREATE TABLE ad_person_group (
    person_id INTEGER,
    group_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES ad_person(id),
    FOREIGN KEY(group_id) REFERENCES ad_group(id)
    );
"""

### Many-to-many mappings
sql_create_person_street = """
CREATE TABLE ad_person_street (
    person_id INTEGER,
    street_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES ad_person(id),
    FOREIGN KEY(street_id) REFERENCES ad_street(id)
    );
"""

### Many-to-many mappings
sql_create_person_email = """
CREATE TABLE ad_person_email (
    person_id INTEGER,
    email_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES ad_person(id),
    FOREIGN KEY(email_id) REFERENCES ad_email(id)
    );
"""

### Many-to-many mappings
sql_create_person_phone = """
CREATE TABLE ad_person_phone (
    person_id INTEGER,
    phone_id INTEGER,
    FOREIGN KEY(person_id) REFERENCES ad_person(id),
    FOREIGN KEY(phone_id) REFERENCES ad_phone(id)
    );
"""