    if txt.find(' ') != -1:
        return txt.split(' ')
    elif txt.find(',') != -1:
        return txt.split(',')
    else:
        count = 0
        for i in range(ord('a'), ord('z') + 1):
            if txt.lower().count(chr(i)) % 2 == 1:
                count += 1
        return count


