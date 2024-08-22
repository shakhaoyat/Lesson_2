fruits=("Mango","orange","banana")

#fruits[1]="apple"
#direct ai vabe change kora jai na trupple age list kore pore change korte hoi

fruits=list(fruits)
fruits[1]="apple"
fruits=tuple(fruits)

print(fruits)

#add korte chai jodi extra kichu
fruits=list(fruits)
fruits.append(1)
fruits.append(2)
fruits.append(3)
fruits=tuple(fruits)
print(fruits)

#remove korte chai jodi kono time

fruits=list(fruits)

fruits.remove(2)

fruits=tuple(fruits)
print(fruits)
