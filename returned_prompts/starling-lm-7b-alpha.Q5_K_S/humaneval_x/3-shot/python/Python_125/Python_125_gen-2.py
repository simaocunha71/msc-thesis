    if ' ' in txt or ',' in txt:
        return txt.split(' ') if ' ' in txt else txt.split(',')
    else:
        count = 0
        for i in txt:
            if i.lower() == i and ord(i) % 2 == 1:
                count += 1
        return count


