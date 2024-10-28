def check_integer(string):
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True