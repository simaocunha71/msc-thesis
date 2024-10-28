    if is_palindrome(string):
        return string

    for idx in range(len(string)):
        postfix = string[idx:]
        if is_palindrome(postfix):
            prefix = string[:idx]
            return string + prefix[::-1]

    return string + string[::-1]


