from datetime import datetime, timedelta

week_days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
month_names = ['Januar', 'Februar', 'Marts', 'April', 'Maj', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'December']


start = datetime(year=2020, month=1, day=1)

month = [{'Mon': [], 'Tue': [], 'Wed': [], 'Thu': [], 'Fri': [], 'Sat': [], 'Sun': []} for i in range(12)]
start_day = []
currMonth = 0
sday = lambda d: datetime.strftime(d, "%a")

for i in range(366):
    d = start + timedelta(days=i)
    if not d.month == currMonth:
        start_day.append( sday(d) )
        currMonth = d.month
    month[d.month-1][ sday(d) ].append(d)

january = month[0]

def print_month(month_num):
    print('= ' * 5 + "%-11s"%month_names[month_num] + ' ='*5)
    m = month[month_num]
    start = start_day[month_num]

    print("   ", end="")
    for w in week_days: print(" %s" % w, end="")
    print("")

    started = False
    for i in range(5):
        line = ""
        for j in range(7):
            started = started or start == week_days[j]
            
            if started:
                day = week_days[j]
                if len(m[day]) == 0: 
                    line += "    "
                    continue
                d = m[day].pop(0)
                line += "%4i" % d.day

            else: line += "    "

        line = "%2i " % d.isocalendar()[1] + line
        print(line)


for i in range(12):
    print_month(i)








