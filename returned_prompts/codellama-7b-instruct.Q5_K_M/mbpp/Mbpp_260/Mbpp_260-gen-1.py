
def newman_prime(n):
    if n == 1:
        return 2
    else:
        return newman_shanks_williams(newman_prime(n-1))

def newman_shanks_williams(n):
    if is_prime(n):
        return n
    else:
        return newman_shanks_williams(newman_prime(n+1))

def is_prime(n):
    if n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
