    if txt.count(' ') > 0:
        return txt.split(' ')
    elif txt.count(',') > 0:
        return txt.split(',')
    else:
        count = 0
        for i in range(len(txt)):
            if ord(txt[i]) % 2 != 0:
                count += 1
        return count


