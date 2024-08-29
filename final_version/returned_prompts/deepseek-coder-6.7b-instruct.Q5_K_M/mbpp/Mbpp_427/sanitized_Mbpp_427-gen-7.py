def change_date_format(date):
    date_list = date.split('-')
    return '{}-{}-{}'.format(date_list[2], date_list[1], date_list[0])