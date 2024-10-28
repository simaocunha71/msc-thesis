
def count_Primes_nums(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n % 2 == 0:
        return count_Primes_nums(n-1)
    if n % 3 == 0:
        return count_Primes_nums(n-2)
    if n % 5 == 0:
        return count_Primes_nums(n-4)
    return count_Primes_nums(n-6)+1


