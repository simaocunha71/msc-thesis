def proper_divisors(n):
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.extend([i, n // i])
    return divisors
def d(n):
    return sum(proper_divisors(n))
def amicable_numbers_sum(n):
    result = 0
    for i in range(1, n+1):
        if i == d(d(i)) and i != d(i):
            result += i
    return result