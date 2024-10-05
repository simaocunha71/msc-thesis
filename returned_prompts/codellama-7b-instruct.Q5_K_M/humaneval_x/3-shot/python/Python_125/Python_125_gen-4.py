    if txt.count(' ') > 0:
        return txt.split()
    elif txt.count(',') > 0:
        return txt.split(',')
    else:
        return sum([1 for i in txt if ord(i) % 2 == 1])
