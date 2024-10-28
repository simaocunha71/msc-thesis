    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for c in txt:
            if c.islower() and (ord(c) - ord('a')) % 2 != 0:
                count += 1
        return count

