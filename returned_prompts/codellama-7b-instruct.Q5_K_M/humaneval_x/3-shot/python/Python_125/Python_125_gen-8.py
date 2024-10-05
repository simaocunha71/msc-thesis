    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return sum([ord(x) % 2 == 0 for x in txt.lower()])

