def amicable_numbers_sum(n):
    amicable_numbers = [sum(divisors(i)) for i in range(1,n+1) if sum(divisors(i))!=i]
    return sum(amicable_numbers)
def divisors(n):
    if n%2==0:
        return [i for i in range(2,n+1,2)]
    else:
        return [i for i in range(3,n+1,2)]