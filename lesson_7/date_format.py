from datetime import datetime
current_date_time=datetime.now()
print(current_date_time)

#starftime()

print(datetime.strftime(current_date_time,"%d/%m/%Y %H:%M:%S"))