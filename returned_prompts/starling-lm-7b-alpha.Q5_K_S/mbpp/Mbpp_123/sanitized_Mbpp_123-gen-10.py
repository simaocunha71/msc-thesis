def amicable_numbers_sum(n):
    if n<1:
        return 0
    amicable_numbers = set()
    for i in range(1,n+1):
        if i==sum(set(divisors(i))-{i}):
            amicable_numbers.add(i)
        if i==sum(set(divisors(sum(set(divisors(i))-{i})))-{sum(set(divisors(i))-{i})}) and i!=sum(set(divisors(i))-{i}):
            amicable_numbers.add(sum(set(divisors(i))-{i}))
    return sum(amicable_numbers)
def divisors(n):
    i = 1
    divisors = []
    while i*i <= n:
        if n%i==0:
            divisors.append(i)
        i += 1
    return divisors