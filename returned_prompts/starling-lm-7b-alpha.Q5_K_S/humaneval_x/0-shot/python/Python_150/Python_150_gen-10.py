    #check if the number is prime
    is_prime = lambda n: all(n % i for i in range(2, int(n ** 0.5) + 1))

    if is_prime(n):
        return x
    else:
        return y


# Tests
print(x_or_y(7, 34, 12)) # 34
print(x_or_y(15, 8, 5)) # 5





def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(x_or_y(7, 34, 12)) # 34
print(x_or_y(15, 8, 5)) # 5



def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(x_or_y(7, 34, 12)) # 34
print(x_or_y(15, 8, 5)) # 5



def x_or_y(n, x, y):
    if is_prime(n):
        return x
    else:
        return y

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(x_or_y