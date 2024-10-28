    if is_palindrome(string):
        return string
    for idx in range(len(string)):
        if is_palindrome(string[idx:]):
            return string + string[:idx][::-1]
    return string + string[::-1]


