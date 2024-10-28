    if x > y or x < 0 or y < 0:
        return -1
    else:
        for i in range(y, x-1, -1):
            if i % 2 == 0:
                return i

        return -1


