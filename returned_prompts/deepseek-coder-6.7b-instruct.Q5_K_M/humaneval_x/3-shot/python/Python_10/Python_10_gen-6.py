    for idx in range(len(string)):
        if is_palindrome(string[idx:]):
            return string[:idx] + string[::-1]


