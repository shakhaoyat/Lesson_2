fruits=("Mango","orange","banana")
for fruit_new in fruits:
    print(fruit_new)
    ##print(fruits)
    ##ata full tuple ti loop a ghurai

print(len(fruits))
#touple ar length hisab kore
for i in range(1,len(fruits)):
    print(fruits[i])

#range dia tuple dia range select kore dewa jai
fruit_1=0
while fruit_1 < len(fruits):
    print(fruits[fruit_1])  # This will print each item in the tuple one by one
    fruit_1 += 1  # Increment fruit_1 to move to the next item in the tuple