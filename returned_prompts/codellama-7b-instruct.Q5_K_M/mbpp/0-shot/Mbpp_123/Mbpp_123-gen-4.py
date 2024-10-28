def amicable_numbers_sum(n):
    s = 0
    for i in range(1, n+1):
        if sum(divisors(i)) == i and sum(divisors(sum(divisors(i)))) == i:
            s += i
    return s

def divisors(n):
    return [i for i in range(1, int(n**0.5)+1) if n % i == 0]


