    if is_palindrome(string):
        return string

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]

    return string + string[::-1]


