    def is_even_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    def is_odd_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    even_count = 0
    odd_count = 0

    for i in range(1, n + 1):
        if is_even_palindrome(i):
            even_count += 1
        if is_odd_palindrome(i):
            odd_count += 1

    return (even_count, odd_count)


