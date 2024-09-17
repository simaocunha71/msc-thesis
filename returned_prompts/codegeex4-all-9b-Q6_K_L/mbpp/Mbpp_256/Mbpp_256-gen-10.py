def count_Primes_nums(n: int) -> int:
    count = 0
    for num in range(2, n):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            count += 1
    return count

