def change_date_format(date):
    date_list = date.split("-")
    return "-".join([date_list[2], date_list[1], date_list[0]])