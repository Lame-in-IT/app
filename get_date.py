from datetime import datetime
from datetime import date, timedelta

def get_date():
    corrent_date = "{:%Y-%m-%d}".format(datetime.now())
    format_date = corrent_date.split("-")
    year = int(format_date[0])
    month_1 = int(format_date[1])
    day = int(format_date[2])
    first_date = date(year, month_1, day)
    duration = timedelta(days=20)
    list_last_day = []
    for d in range(duration.days + 1):
        day = first_date - timedelta(days=d)
        list_last_day.append(day)
    last_day = list_last_day[1]
    return [corrent_date, last_day]

if __name__ == '__main__':
    get_date()