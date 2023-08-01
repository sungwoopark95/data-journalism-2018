from datetime import datetime
from time import strftime

now = datetime.now()
def calendar_module():
    year = strftime("%Y")
    month = strftime("%m")
    day = strftime('%d')
    date = now.day
    remain_date = 30 - date + 31 + 31 + 25
    class_count = input("이제까지 수업을 몇 번 하셨습니까?: ")
    remain_class = 15 - int(class_count)
    print("오늘은 %s년 %s월 %s일, 크리스마스까지는 %d일이나 남았네. 이 수업도 이제 %d번밖에 안 남았구나!" %(year, month, day, remain_date, remain_class))

calendar_module()