import datetime
def change_date_format(date):
    date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    return date_object.strftime('%d-%m-%Y')