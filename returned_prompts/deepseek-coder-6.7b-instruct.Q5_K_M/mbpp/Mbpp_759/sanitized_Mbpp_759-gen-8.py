def is_decimal(s):
    try:
        float(s)
        if "." in s:
            split_dec = s.split(".")
            if len(split_dec[1]) == 2:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False