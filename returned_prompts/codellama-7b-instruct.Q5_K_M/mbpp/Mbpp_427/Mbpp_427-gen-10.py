
def change_date_format(date_string: str) -> str:
    return '-'.join(reversed(date_string.split('-')))


