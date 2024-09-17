
def sum_of_divisors(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        elif i * (n // i) == n:
            sum = sum + i + n//i
            i += 1
    return sum

def amicable_numbers_sum(n):
    result = 0
    for i in range(2, n+1):
        if sum_of_divisors(i) > i and sum_of_divisors(sum_of_divisors(i)) == i:
            result += i
    return result


