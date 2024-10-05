    if txt.find(' ') != -1:
        return txt.split(' ')
    if txt.find(',') != -1:
        return txt.split(',')
    count = 0
    for i in range(len(txt)):
        if (ord(txt[i]) - ord('a')) % 2 == 1:
            count += 1
    return count


