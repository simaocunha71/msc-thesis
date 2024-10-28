def change_date_format(date_str):
    date_list = date_str.split("-")
    return f"{date_list[1]}-{date_list[0]}-{date_list[2]}"