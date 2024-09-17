def sum_divisors(n1,n2):
    common_divisors = set(range(1, min(n1, n2)+1))
    for i in range(2, min(n1, n2)+1):
        if n1 % i == 0 and n2 % i == 0:
            common_divisors.add(i)
    return sum(common_divisors)

