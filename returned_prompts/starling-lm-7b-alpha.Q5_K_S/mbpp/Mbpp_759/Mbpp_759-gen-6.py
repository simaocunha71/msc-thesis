
def is_decimal(str):
    try:
        float(str)
        if str.count('.') == 1 and str.count('.') != 2:
            return True
        else:
            return False
    except ValueError:
        return False


