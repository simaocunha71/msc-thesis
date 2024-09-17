def check_monthnumb_number(month_number: int) -> bool:
    if month_number in [4, 6, 9, 11]:
        return False
    elif month_number == 2:
        return True
    else:
        return True