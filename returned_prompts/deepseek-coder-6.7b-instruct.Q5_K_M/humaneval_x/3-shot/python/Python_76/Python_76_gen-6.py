    i = 1
    while True:
        power = n ** i
        if power == x:
            return True
        elif power > x:
            return False
        i += 1


