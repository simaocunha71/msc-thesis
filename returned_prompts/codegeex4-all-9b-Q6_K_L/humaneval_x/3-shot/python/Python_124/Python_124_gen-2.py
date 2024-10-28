    import datetime

    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
        return True
    except ValueError:
        return False

