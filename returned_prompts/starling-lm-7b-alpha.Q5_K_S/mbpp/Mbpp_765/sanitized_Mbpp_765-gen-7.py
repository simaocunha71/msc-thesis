def is_polite(num):
    if num == 1:
        return True
    elif num % 2 == 0:
        return False
    elif num % 2 != 0:
        return is_polite(num - 2)