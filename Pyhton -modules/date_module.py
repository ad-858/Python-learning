import datetime
x=datetime.datetime.now()
print(x)
# date class
td=datetime.date.today()
print(td)
print(td.year)
print(td.month)
print(td.day)
print(td.weekday())
print(td.isoweekday())
# timedelta() is use to calculate the difference between two dates or time
bday=datetime.date(2022,10,5)
till_day=(bday-td)
print(till_day.total_seconds())
print(till_day.days)
# time class
t= datetime.time(18,13,50,100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
# datetime
dt=datetime.datetime(2022,4,25,18,15,36,100000)
print(dt)
print(dt.date())
print(dt.time())
print(dt.year)
print(x.date())
x=datetime.datetime.now()
print(x)
x=datetime.datetime.utcnow()
print(x)
x=datetime.datetime.today()
print(x)
x=datetime.datetime.now()
print(x.strftime("%a"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%b"))
print(x.strftime("%B"))
print(x.strftime("%w"))
print(x.strftime("%u"))
print(x.strftime("%G"))
print(x.strftime("%V"))
print(x.strftime("%j"))
print(x.strftime("%f"))
print(x.strftime("%c"))
print(x.strftime("%Y-""%m-""%d"" ""%H:""%M:""%S"" ""%p"))
