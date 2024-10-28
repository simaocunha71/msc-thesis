    from datetime import datetime

    date_string = date
    date_format = "%m-%d-%Y"

    try:
        datetime.strptime(date_string, date_format)
        return True
    except ValueError:
        return False


