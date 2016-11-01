#!/usr/bin/env python2
# coding: utf-8

from bookmanager import BookManager

bm=BookManager()

# TEST 1: add person to the address book
print("### TEST 1 : create person ###")
p = bm.createPerson('Alex', 'Long')
p2 = bm.createPerson('Lily', 'Green')

if p:
    print("Passed")
    print(p)
    print(p2)
else:
    print("Failed")

# TEST 2: add group to the address book
print("### TEST 2 : create group ###")
g = bm.createGroup('Linux')
g2 = bm.createGroup('Windows')

if g:
    print("Passed")
    print(g)
    print(g2)
else:
    print("Failed")



#################
## Preparation for Test 3, 4, 5, 6 ...
#################
# add person to groups: Add 'Alex' to 2 groups  Linux and Windows
flag = bm.addGroupToPerson(p, g)
bm.addGroupToPerson(p, g2)

# add person to groups: Add 'Lily' to a group Linux
bm.addGroupToPerson(p2, g)



#################
## End of Preparation for Test 3, 4, 5, 6 ...
#################

# TEST 3: Given a group we want to easily find its memebers
print("### TEST 3 : find members of a group 'Linux' ###")
persons_in_linux_group =  bm.getGroupMembers(group="Linux")

# test if 'Alex' and 'Lily' is in the group
assert p in persons_in_linux_group
assert p2 in persons_in_linux_group

print("Passed")
print(persons_in_linux_group)


# TEST 4: Given a person we want to easily find the groups the person blongs to
# in this case 'Alex' belongs to group 'Linux' and 'Windows'
print("### TEST 4 : find groups he belongs to 'Alex' ###")
groups_of_alex =  bm.getGroupsByPerson('Alex')
assert g in groups_of_alex
assert g2 in groups_of_alex

if (len(bm.getGroupsByPerson('Alex')) == 2):
    print("Passed")
    print(groups_of_alex)
else:
    print("Failed")

# TEST 5: Find person by name ( can supply either firstname, last name, or both )
print("### TEST 5 : find person by name 'Alex' ###")
the_person = bm.getPersonByName('Alex Long')
assert p == the_person[0]
print("Passed")
print the_person




# TEST 6: Find person by email address (can supply either the exact string or a prefix string, ie. both "alexander@company.com" and "alex" should work).
print("### TEST 6 : get person who have email alexander@company.com or only the prefix alex ###")

# create email
my_email = bm.createEmail('alexander@company.com')

# add email 'ab@cd.com' to person 'Alex'
flag2 = bm.addEmailToPerson(p, my_email)

# print(flag2)


those_who_have_this_email_prefix =  bm.getPersonByEmail('alexander')

assert p in those_who_have_this_email_prefix 

# print bm.getPersonByEmail('nobody@nobody.com')

print("Passed")

print(those_who_have_this_email_prefix)
