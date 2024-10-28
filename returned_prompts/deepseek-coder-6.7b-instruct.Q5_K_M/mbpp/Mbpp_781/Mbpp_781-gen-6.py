
def count_divisors(n):
    count = 0
    i = 1
    while(i <= n):
        if (n % i == 0):
            count += 1
        i = i + 1
    return count % 2 == 0


