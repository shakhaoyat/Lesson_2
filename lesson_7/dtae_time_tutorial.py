import datetime
#current datetime
print(datetime.datetime.now())
#current_utc time
print(datetime.datetime.utcnow())
#get date

print(datetime.date.today())
#timestamp

print(datetime.date.fromtimestamp(123456789))
random_date=datetime.date.fromtimestamp(123456789)
print(type(random_date))
print(random_date.year)
print(random_date.month)
print(random_date.day)


