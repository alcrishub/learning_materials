import random
random_number = random.randint(1, 100)
import datetime
now = datetime.datetime.now()
current_year = now.year
print(random_number)
print(now)
print(current_year)

future = now + datetime.timedelta(days=48)
print(future)