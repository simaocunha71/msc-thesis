def odd_num_sum(n):
    return sum(i**4 for i in range(1, 2*n, 2))  # calculate sum of fourth power of first n odd natural numbers