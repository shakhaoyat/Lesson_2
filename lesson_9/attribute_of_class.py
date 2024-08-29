class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


#method  create

#methor means function inside a class
    def introduce(self):
        return "my name is {}".format(self.name)



person_one=Person("shakhaoyat",26,"male")

print(person_one.name)
print(person_one.age)
print(person_one.gender)

person_two=Person("chad",24,"male")
print(person_two.name)
print(person_two.age)
print(person_two.gender)



#methord call


print(person_one.introduce())
print(person_two.introduce())