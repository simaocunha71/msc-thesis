    if n % 2 == 1:
        return False
    else:
        while n > 4:
            if n % 4 == 0:
                n -= 4
            else:
                return False
    return True


