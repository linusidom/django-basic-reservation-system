import datetime

print(datetime.datetime.now().strftime('%Y-%m-%d 08:00:00.0'))

print(datetime.time())

print(datetime.date.today())

with open("./appointments/models.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print(i, repr(line))