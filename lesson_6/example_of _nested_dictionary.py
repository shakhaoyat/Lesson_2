courses={
    1:{

        "name":"c",
        "duration":4
    },

    2:{
        "name":"python",
        "duration":7
    }
}
print(courses)
print(courses[1])
print(courses[2])

#accesss korte pari kono item
print(courses[1]["duration"])
print(courses[2]["name"])


#kono idem modify korte pari

courses[2]["duration"]=1000
courses[2]["add instractor"]="nur"

print(courses[2]["duration"])
print(courses[2])

