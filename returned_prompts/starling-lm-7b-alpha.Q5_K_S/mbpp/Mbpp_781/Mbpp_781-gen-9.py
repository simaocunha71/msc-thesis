"""
def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def is_even(count):
    if count % 2 == 0:
        return True
    else:
        return False

def check_even_divisors(n):
    count = count_divisors(n)
    return is_even(count)

print(check_even_divisors(10))
"""

"""
def check_even_divisors(n):
    if len([i for i in range(1,n+1) if n%i==0]) % 2 == 0:
        return True
    else:
        return False
print(check_even_divisors(10))
"""

