    if a == 0 or a == 1:
        return True
    else:
        for i in range(1, a):
            if i ** 3 == a:
                return True
        return False


