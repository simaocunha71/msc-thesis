def amicable_numbers_sum(n):
    sum_amicable = 0
    for num in range(1, n+1):
        sum_divisors = sum_of_divisors(num)
        if sum_divisors != num and sum_of_divisors(sum_divisors) == num:
            sum_amicable += num
    return sum_amicable
def sum_of_divisors(n):
    sum_divisors = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors