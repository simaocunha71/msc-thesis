def change_date_format(date_str):
    return date_str[8:10] + '-' + date_str[5:7] + '-' + date_str[0:4]  # Python 3.6+