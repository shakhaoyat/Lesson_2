"""
.format()
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}
The placeholders can be identified using
    - named indexes {price},
    - numbered indexes {0},
    - empty placeholders {}.
"""

first_name = "Sifat"
last_name = "Hassan"
user_id = 14

full_name = "{first_name} {last_name} and user id is {user_id}" \
            "".format(
    first_name=first_name,
    last_name=last_name,
    user_id=user_id
)
print(full_name)






# The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.



#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)