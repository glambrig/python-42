import time
import datetime

str = str(time.time())

str = str.split('.')[0]

print(f"Seconds since January 1st, 1970: {int(str):,} or {int(str):e} in scientific notation")

str = datetime.datetime.now()

print(str.strftime("%b"), str.strftime("%d"), str.strftime("%Y"))