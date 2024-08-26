employe={'name': 'shakhaoyat', 'skill': ['python', 'django', 'go'], 'experiance': 4, 'company': 'hult prize', 'address': 'newmarket', 'type': 'present'}

#keys()


print(employe.keys())


#value()

print(employe.values())


#items

print(employe.items())

#loop a use kora ar way

for i in employe.keys():
    print(i,employe[i])
