    prime_num = 0
    max_num = 0
    for i in lst:
        if i > max_num:
            max_num = i

    for i in range(2, max_num):
        for j in range(2, max_num):
            if i * j == max_num:
                prime_num = prime_num + 1

    return len(str(prime_num))
