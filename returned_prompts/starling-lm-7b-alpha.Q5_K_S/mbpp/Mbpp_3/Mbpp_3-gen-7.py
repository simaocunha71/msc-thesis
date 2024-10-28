"""
def is_not_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return True
        else:
            return False
    else:
        return True

assert is_not_prime(2) == False
"""

