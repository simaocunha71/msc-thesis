    def is_palindrome(s):
        return s == s[::-1]

    s = string
    while not is_palindrome(s):
        s = s[1:] + s[0]

    return s


