def change_date_format(date_str: str) -> str:
    date_list = date_str.split("-")
    return "-".join(date_list[::-1])