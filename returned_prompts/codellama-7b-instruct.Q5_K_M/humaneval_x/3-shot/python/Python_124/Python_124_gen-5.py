    import datetime
    def valid_date(date):
        if date == '':
            return False
        elif datetime.datetime.strptime(date, '%m-%d-%Y') > datetime.datetime.now():
            return False
        elif (datetime.datetime.strptime(date, '%m-%d-%Y').day < 1 or datetime.datetime.strptime(date, '%m-%d-%Y').day > 31) and (datetime.datetime.strptime(date, '%m-%d-%Y').month == 2 and datetime.datetime.strptime(date, '%m-%d-%Y').day > 29) and (datetime.datetime.strptime(date, '%m-%d-%Y').month in [4, 6, 9, 11] and datetime.datetime.strptime(date, '%m-%d-%Y').day > 30) and (datetime.datetime.strptime(date, '%m-%d-%Y').month in [1, 3, 5, 7, 8, 10, 12] and datetime.datetime.strptime(date, '%m-%d-%Y').day > 31):
            return False
        elif not datetime.datetime.strptime(date, '%m-%d-%Y').month in range(1, 13):
            return False
        elif not datetime.datetime.strptime(date, '%m-%d-%Y').day in range(1, 32):
            return False
        else:
            return True

    return valid_date(date)
