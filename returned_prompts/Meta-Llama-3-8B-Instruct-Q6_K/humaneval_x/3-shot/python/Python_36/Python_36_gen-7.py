    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            str_num = str(i)
            count += str_num.count('7')

    return count


