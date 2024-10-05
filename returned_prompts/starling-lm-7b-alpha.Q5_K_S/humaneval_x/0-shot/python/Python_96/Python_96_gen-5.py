
def count_up_to(n):
    prime_arr = []
    for i in range(2,n):
        if is_prime(i):
            prime_arr.append(i)
    return prime_arr

def is_prime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f +=6
    return True


count_up_to(5) => [2,3]
count_up_to(11) => [2,3,5,7]
count_up_to(0) => []
count_up_to(20) => [2,3,5,7,11,13,17,19]
count_up_to(1) => []
count_up_to(18) => [2,3,5,7,11,13,17]
































































































































































































