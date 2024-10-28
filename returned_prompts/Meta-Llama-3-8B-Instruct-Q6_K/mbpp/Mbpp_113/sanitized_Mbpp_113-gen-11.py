def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    # if s.isdigit():
    #     return True
    # else:
    #     return False