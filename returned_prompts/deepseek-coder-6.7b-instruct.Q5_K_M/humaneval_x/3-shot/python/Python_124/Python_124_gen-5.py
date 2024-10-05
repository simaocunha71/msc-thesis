    import re
    from datetime import datetime

    date_format = "%m-%d-%Y"

    if re.match(r'\d{2}-\d{2}-\d{4}$', date):
        try:
            datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False
    else:
        return False


