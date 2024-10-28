def change_date_format(date: str) -> str:
    return date[6:8] + '-' + date[4:6] + '-' + date[:4]