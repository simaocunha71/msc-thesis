
def valid_date(date):
    day_month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_month_dict[2] = 29
    month_day_dict = {'03':[1, 31], '04':[1, 30], '05':[1, 31], '06':[1, 30], '07':[1, 31], '08':[1, 31], '09':[1, 30], '10':[1, 31], '11':[1, 30], '12':[1, 31]}
    month_day_dict[2] = [1, 28] + [1, 29]
    date_list = date.split('-')
    if len(date_list) != 3:
        return False
    if len(date_list[0]) != 2 or len(date_list[1]) != 2 or len(date_list[2]) != 4:
        return False
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    if month > 12 or month < 1:
        return False
    if day > day_month_dict[month][1] or day < day_month_dict[month][0]:
        return False
    if year < 1000 or year > 9999:
        return False
    return True

# valid_date('03-11-2000') => True
# valid_date('15-01-2012') => False
# valid_date('04-0-2040') => False
# valid_date('06-04-2020') => True
#