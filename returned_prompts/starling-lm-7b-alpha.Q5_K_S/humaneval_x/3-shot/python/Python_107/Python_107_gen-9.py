    def is_palindrome(n):
        n_str = str(n)
        return n_str == n_str[::-1]

    def is_even(n):
        return n % 2 == 0

    def is_odd(n):
        return n % 2 != 0

    even_count = 0
    odd_count = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if is_even(i):
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)


