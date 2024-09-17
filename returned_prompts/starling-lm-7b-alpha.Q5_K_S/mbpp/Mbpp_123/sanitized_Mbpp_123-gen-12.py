def amicable_numbers_sum(n):
    amicable_numbers = []
    for number in range(1, n+1):
        sum_of_proper_divisors = sum(divisors(number))
        if sum_of_proper_divisors != 1:
            continue
        divisors = divisors(number)
        divisors.append(number)
        if number in divisors:
            continue
        amicable_numbers.append(number)
    return sum(amicable_numbers)
def divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    divisors.sort()
    return divisors