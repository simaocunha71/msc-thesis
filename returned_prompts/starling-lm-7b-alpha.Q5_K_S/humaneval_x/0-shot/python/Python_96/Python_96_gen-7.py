
def count_up_to(n):
    primes = [2]
    for i in range(3,n+1):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(0))
# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(18))


def count_up_to(n):
    primes = [2]
    for i in range(3,n+1):
        if all(i % j != 0 for j in primes):
            primes.append(i)
    return primes


# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(0))
# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(18))



def count_up_to(n):
    primes = [2]
    for i in range(3,n+1):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(0))
# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(18))


def count_up_to(n):
    primes = [2]
    for i in range(3,n+1):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes