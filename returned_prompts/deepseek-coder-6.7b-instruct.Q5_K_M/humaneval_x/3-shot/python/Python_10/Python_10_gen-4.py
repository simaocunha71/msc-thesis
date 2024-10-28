    if is_palindrome(string):
        return string

    for idx in range(len(string), -1, -1):
        if is_palindrome(string[idx:]):
            return string + string[:idx][::-1]


