def amicable_numbers_sum(n):
    total_sum = 0
    for i in range(1, n+1):
        sum1, sum2 = 0, 0
        for j in range(1, i):
            if i % j == 0:
                sum1 += j
        for k in range(1, sum1):
            if sum1 % k == 0:
                sum2 += k
        if sum1 == sum2 and i != sum1:
            total_sum += i
    return total_sum