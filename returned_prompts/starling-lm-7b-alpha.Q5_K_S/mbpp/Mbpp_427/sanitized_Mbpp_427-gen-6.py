def change_date_format(date_str):
    y = date_str[0:4]
    m = date_str[5:7]
    d = date_str[8:]
    return d + "-" + m + "-" + y