
def odd_num_sum(n):
    sum = 0
    for i in range(1, n*2+1, 2):
        sum += i ** 4
    return sum


