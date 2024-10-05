    if txt.find(',') == -1 and txt.find(' ') == -1:
        return [chr(x) for x in range(ord('a'), ord('z') + 1) if x % 2 != 0]
    elif txt.find(',') == -1:
        return txt.split()
    else:
        return txt.split(',')


