def odd_num_sum(n):
    sum = 0
    for i in range(2*n):
        if i % 2 != 0:
            sum += i**4
    return sum