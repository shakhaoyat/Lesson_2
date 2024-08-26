employe={'name': 'shakhaoyat', 'skill': ['python', 'django', 'go'], 'experiance': 4, 'company': 'hult prize', 'address': 'newmarket', 'type': 'present'}

print(employe)

#del keyword

del employe["type"]

print(employe)

#pop() method
employe.pop("address")
print(employe)


#ata delete kora value return korbe
print(employe.pop("company"))
print(employe)