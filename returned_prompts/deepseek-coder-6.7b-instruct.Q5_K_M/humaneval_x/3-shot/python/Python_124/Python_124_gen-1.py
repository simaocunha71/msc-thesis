    from datetime import datetime
    try:
        datetime.strptime(date, '%m-%d-%Y')
        return True
    except ValueError:
        return False


