

import datetime
import pytz

timeZ_Po = pytz.timezone('America/Los_Angeles')
timeZ_Ny = pytz.timezone('America/New_York')
timeZ_Lo = pytz.timezone('Europe/London')

dt_Po = datetime.datetime.now(timeZ_Po)
dt_Ny = datetime.datetime.now(timeZ_Ny)
dt_Lo = datetime.datetime.now(timeZ_Lo)

if int(dt_Po.strftime('%H')) > 9 and int(dt_Po.strftime('%H')) < 17:
    print("The Portland store is open.")
else:
    print("The Portland store is closed.")

if int(dt_Ny.strftime('%H')) > 9 and int(dt_Ny.strftime('%H')) < 17:
    print("The New York store is open.")
else:
    print("The New York store is closed.")

if int(dt_Lo.strftime('%H')) > 9 and int(dt_Lo.strftime('%H')) < 17:
    print("The London store is open.")
else:
    print("The London store is closed.")
