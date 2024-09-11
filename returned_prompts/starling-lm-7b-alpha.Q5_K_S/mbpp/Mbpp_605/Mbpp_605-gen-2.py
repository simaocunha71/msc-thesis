"""
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
"""


def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def prime_num_generator(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            yield False
            break
    yield True


assert prime_num(13) == True
assert prime_num(12) == False


def prime_num_generator_2(n):
    if n <= 1:
        yield False
        return
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            yield False
            break
    yield True


assert all(map(prime_num_generator, [13, 12]))

def prime_num_generator_3(n):
    if n <= 1:
        return (False,)
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return (False,)
    return (True,)


assert tuple(map(prime_num_generator_3, [13, 12])) == (True, False)

def prime_num_generator_4(n):
    if n <= 1:
        return [False]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return [False]
    return [True]


assert prime_num_generator_4(13) == [True]
assert prime_num_generator_4(12) == [False]

def prime_num_generator_5(n):
    if n