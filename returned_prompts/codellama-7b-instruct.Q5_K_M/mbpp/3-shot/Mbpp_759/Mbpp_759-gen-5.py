
def is_decimal(num: str):
    try:
        float(num)
    except ValueError:
        return False
    else:
        if len(num) > 3:
            return False
        return True


