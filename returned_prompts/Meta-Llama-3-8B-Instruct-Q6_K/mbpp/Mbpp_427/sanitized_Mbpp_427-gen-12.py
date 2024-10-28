import datetime
def change_date_format(date):
    try:
        dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        return dt.strftime('%d-%m-%Y')
    except ValueError:
        return "Invalid date format"