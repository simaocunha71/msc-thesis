def is_decimal(s):
    if "." not in s:
        return False
    if s.split(".")[1] > "99":
        return False
    if not s.split(".")[0].isdigit():
        return False
    return True