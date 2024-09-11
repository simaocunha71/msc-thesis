"""
def count_Primes_nums(n):
    primes = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return len(primes)

print(count_Primes_nums(5))
"""

