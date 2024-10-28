
def sum_of_common_divisors(n1, n2):
    divisors = []
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            divisors.append(i)
    return sum(divisors)


