def d(n):
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i
            if i * i != n:
                sum += n // i
    return sum
def amicable_numbers_sum(n):
    res = 0
    for i in range(2, n + 1):
        if d(i) > i and d(d(i)) == i:
            res += i
    return res