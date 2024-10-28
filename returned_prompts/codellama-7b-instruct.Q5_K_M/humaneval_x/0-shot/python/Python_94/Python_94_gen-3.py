

def skjkasdkd(lst):
    largest_prime = 0
    largest_prime_sum = 0
    for i in lst:
        if is_prime(i):
            if i > largest_prime:
                largest_prime = i
                largest_prime_sum = sum(str(i))
    return largest_prime_sum

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
