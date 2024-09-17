def check_integer(s: str):
    try:
        int(s)
        return True
    except ValueError:
        return False