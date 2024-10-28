    def is_palindrome(x):
        return str(x) == str(x)[::-1]

    even_count = sum(1 for i in range(1, n + 1) if is_palindrome(i) and i % 2 == 0)
    odd_count = sum(1 for i in range(1, n + 1) if is_palindrome(i) and i % 2 != 0)

    return (even_count, odd_count)


