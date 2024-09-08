def divisors(n):
    divs = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                divs.append(i)
            else:
                divs.extend([i, n // i])
    return divs
def amicable_numbers_sum(limit):
    numbers = [0] * (limit+1)
    for i in range(1, limit+1):
        numbers[i] = sum(divisors(i))
    return sum(i for i in range(1, limit+1) if i < numbers[i] and numbers[numbers[i]] == i)