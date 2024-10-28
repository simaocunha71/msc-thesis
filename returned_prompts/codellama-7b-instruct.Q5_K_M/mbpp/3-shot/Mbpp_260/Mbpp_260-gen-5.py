
def newman_prime(n: int) -> int:
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 11
    else:
        i = 2
        while i ** 2 <= n:
            i += 1
        while True:
            j = 2
            while j <= i:
                if i % j == 0:
                    break
                j += 1
            if j == i:
                return i
            i += 1


