def is_polite(num):
    if (num == 1):
        return True
    if (num % 2 != 0):
        return False
    if (is_polite(num / 2)):
        return True
    else:
        return False