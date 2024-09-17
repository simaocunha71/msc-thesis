def change_date_format(date):
    date_list = date.split('-')
    return date_list[1] + '-' + date_list[0] + '-' + date_list[2]