    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_num = str(i)
            if '7' in str_num:
                count += 1
    return count


