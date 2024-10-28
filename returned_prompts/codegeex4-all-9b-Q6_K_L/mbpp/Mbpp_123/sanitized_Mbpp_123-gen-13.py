def amicable_numbers_sum(n):
    def divisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum
    sum = 0
    for i in range(2, n+1):
        j = divisors(i)
        if i != j and i == divisors(j):
            sum += i
    return sum