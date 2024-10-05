    from collections import deque
    import sys

    def has_even(x):
        while x > 0:
            if x % 10 % 2 == 0:
                return True
            x //= 10
        return False

    queue = deque(filter(has_even, x))
    queue.sort()
    return queue




def has_even(x):
    while x > 0:
        if x % 10 % 2 == 0:
            return True
        x //= 10
    return False


def unique_digits(x):
    queue = deque(filter(has_even, x))
    queue.sort()
    return queue


def unique_digits_slow(x):
    res = []
    for i in x:
        if not any(j % 2 == 0 for j in str(i)):
            res.append(i)
    res.sort()
    return res



if __name__ == "__main__":
    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))
















































































































































































































