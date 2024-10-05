    num_list = [int(x, 16) for x in num]
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for i in num_list:
        for j in prime_list:
            if i % j == 0:
                count += 1
    return count


