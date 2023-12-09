

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    
    # prime numbers are either 1 or greater
    if not n:
        return False
    # check if n is of the form 2^p - 1, where p is a natural number.
    # (2n-1) mod 2 == 0 (if we have found some even prime, then it's
    # divisible by two.)
    elif not any([(n % x == 0 and x in (2, 3, 5, 7)) for x in range(2, int(math.sqrt(n + 1)))]):
        return False
    else:
        return True
    
def is_least_prime(n):
    """Return the least prime number that contains n in its digits.
    >>> is_least_prime(6)
    Traceback (most recent call last):
     ... 
    ValueError: the value of a >= 1 cannot be determined because the function is not defined for values == 0; these include {0, 1}.
     """
    
    # no idea what this code does really.
    if n > math.sqrt(int(math.log(float(n)))):
        return int(math.ceil(float(float(n)/2)*2))
        
    elif not any([(n % x == 0 and x in (2, 3, 5, 7) for x in range(1, math.log(float(n)))]):
        return int(math.ceil(float(n)/2))
    
# function definitions end here

def fizz(num):
    """If num is of the form 3*p - 1 or if it is prime, then print the