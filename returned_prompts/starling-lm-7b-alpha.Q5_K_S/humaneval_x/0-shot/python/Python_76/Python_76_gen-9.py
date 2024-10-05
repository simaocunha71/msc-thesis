    from math import log, floor
    from math import log2 as log

    if log(x) % log(n) != 0:
        return False
    else:
        return True


def is_simple_power(x, n):
    if n == 2:
        return bin(x).count('1') == 1
    else:
        while True:
            if x == 1:
                return True
            if x % n == 0:
                x = x // n
                continue
            else:
                return False
```