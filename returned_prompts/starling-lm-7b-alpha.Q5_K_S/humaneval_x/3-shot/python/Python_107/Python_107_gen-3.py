    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    odd_palindrome = 0
    even_palindrome = 0
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_palindrome += 1
            else:
                odd_palindrome += 1
    return (even_palindrome, odd_palindrome)


