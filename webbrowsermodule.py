import webbrowser as wb
import datetime


wb.open("https://www.python.org")

wb.open("https://www.kibu.ac.ke")

print(datetime.datetime.now())


from datetime import datetime
import pytz

# current Datetime
unaware = datetime.now()
print('Timezone naive:', unaware)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)

# US/Central timezone datetime
aware_us = datetime.now(pytz.timezone('US/Central'))
print('US Central DateTime', aware_us)
