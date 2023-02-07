from datetime import datetime, timedelta,date
from dateutil.parser import parse


class DataRasp:

    def __init__(self):
        pass

    def date_min(self) -> str:
        now_day = datetime.now()
        return f"{now_day.strftime('%Y-%m-%d')}T{now_day.strftime('%H:%M')}"

    def sum_date(self,date_lesson):
        date = date_lesson
        dt = parse(date)
        date_timestart = str(dt).split(' ')
        ts = datetime.timestamp(dt) + 5400 #длительность пары в секундах
        date_time = datetime.fromtimestamp(ts)
        date_end = str(date_time).split(' ')[1]
        return date_timestart[0],date_timestart[1][:-3],date_end[:-3]


if __name__ == '__main__':
    date_time = DataRasp()
    print(date_time.date_min())
    # print(date_time.sum_date())
