    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    def is_odd(x):
        return x % 2 != 0

    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if is_palindrome(i):
            if is_odd(i):
                odd_count += 1
            else:
                even_count += 1

    return (even_count, odd_count)


