#strptime()

from datetime import datetime
book_date="03,March,2024"
book_creation_actual_date=datetime.strptime(book_date,"%d,%B,%Y")
print(type(book_creation_actual_date))
print(book_creation_actual_date)
