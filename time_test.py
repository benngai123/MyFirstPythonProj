import time

# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

import datetime

print(datetime.datetime.now())
new_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + new_time)

one_day = datetime.datetime(2008, 5, 27)
new_date = datetime.timedelta(days=10)
print(one_day + new_date)
