Notes and test codes
==================

This isn't a part of module `bookmanager` but a test field for development, recording codes and notes before production.

What is an address book?
------------------------

It should be a model which looks like that one instance can point to many intances for a many to many relationship.

I tried to write pure models in Python only with some class(es), list, matrix or so. But I found the relationship part is not so handy and efficent. Mostly I am inventing wheels... 

After a while of consideration, I decided to use something running in RAM. So the Python built-in database SQLite came to my mind. 

Then I wrote a model `sql_models.py` to map all the **many to many** relationships between different real things. But I found manupilating it could be very exhaused because I have to write all the SQL Python wrapper by hands...

It's 21st century, re-inventing SQL Python wrappers is not as difficult as landing on the moon. But I don't have so much time doing this re-inventing. So I used `SQLAlchemy` -- A powerful ORM in Python. 

Later on, writting a wrapper on top of SQLAlchemy is very productive. 

Then a new module `bookmanager` came out. 

It runs in RAM, mapping all objects dynamically.
