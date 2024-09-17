def amicable_numbers_sum(n):
    amicable_numbers = []
    for i in range(1,n+1):
        sum_divisors = sum_divisors(i)
        if sum_divisors != i:
            divisors = find_divisors(sum_divisors)
            for j in divisors:
                if j != i:
                    if sum_divisors(j) == i:
                        amicable_numbers.append(i)
                        break
    return sum(amicable_numbers)
def find_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors
def sum_divisors(n):
    sum = 0
    for i in range(1,n+1):
        if n%i == 0:
            sum += i
    return sum