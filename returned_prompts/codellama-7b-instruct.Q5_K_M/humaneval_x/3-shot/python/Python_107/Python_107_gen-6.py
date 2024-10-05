    num_of_even, num_of_odd = 0, 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                num_of_even += 1
            else:
                num_of_odd += 1
    return num_of_even, num_of_odd


