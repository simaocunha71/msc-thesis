
    # count_one_starts = count_one_ends = 0
    # for i in range(10**(n-1), 10**n):
    #     if str(i)[0] == '1':
    #         count_one_starts += 1
    #     if str(i)[-1] == '1':
    #         count_one_ends += 1
    # return count_one_starts + count_one_ends

    count_one_starts = count_one_ends = 0
    for i in range(10**(n-1), 10**n):
        if str(i)[0] == '1':
            count_one_starts += 1
        if str(i)[-1] == '1':
            count_one_ends += 1
    return count_one_starts + count_one_ends



