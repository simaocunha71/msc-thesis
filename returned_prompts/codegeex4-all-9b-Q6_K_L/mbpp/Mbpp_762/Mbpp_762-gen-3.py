def check_monthnumber_number(month: int) -> bool:
    if month in [4, 6, 9, 11]:
        return False
    else:
        return True