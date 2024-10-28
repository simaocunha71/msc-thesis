def next_smallest_palindrome(n):
    def is_palindrome(num):
        num_str = str(num)
        return num_str == num_str[::-1]

    while True:
        if is_palindrome(n + 1):
            return n + 1
        n += 1