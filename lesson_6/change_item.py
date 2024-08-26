employe={"name":"shakhaoyat","skill":["python","django","go"],
         "experiance":4}

print(employe["name"])
employe["name"]="chad"
print(employe["name"])
employe["experiance"]=9
print(employe["experiance"])


#update method

employe.update(

{
    "name":"hossain",
    "experiance":100
}

)

print(employe)