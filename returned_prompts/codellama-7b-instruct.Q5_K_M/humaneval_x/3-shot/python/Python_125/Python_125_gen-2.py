    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        count = 0
        for i in range(26):
            if txt.lower().count(chr(97+i)) % 2 == 1:
                count += 1
        return count


