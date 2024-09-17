def amicable_numbers_sum(n: int) -> int:
    sum = 0
    for i in range(1, n+1):
        if d(i) == i:
            continue
        if d(d(i)) == i:
            sum += i
    return sum
def d(n):
    sum = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            sum += i
            if n // i != i:
                sum += n // i
    return sum