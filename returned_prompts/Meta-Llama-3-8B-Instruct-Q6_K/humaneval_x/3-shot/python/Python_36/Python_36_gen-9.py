    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            if '7' in str_i:
                count += str_i.count('7')

    return count


