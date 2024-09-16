def is_nonagonal(n):
    return (n * (3 * n - 1)) // 2 == 10**n

def find_nth_nonagonal(n):
    return nth_number(is_nonagonal, n)

def nth_number(test, n):
    for i in range(1, n+1):
        if test(i):
            return i
    return None
