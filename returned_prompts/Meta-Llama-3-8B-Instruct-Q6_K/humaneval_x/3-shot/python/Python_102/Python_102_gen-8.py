    if x % 2 == 0:
        if y % 2 == 0:
            return y
        else:
            for i in range(y-1, x-1, -1):
                if i % 2 == 0:
                    return i
            return -1
    else:
        for i in range(x+1, y+1):
            if i % 2 == 0:
                return i
        return -1
    return -1


