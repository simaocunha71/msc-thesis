    if is_palindrome(string):
        return string

    for i in range(len(string)):
        prefix = string[:i]
        postfix = string[i:]
        if is_palindrome(postfix):
            return string + prefix[::-1]

    return string + string[::-1]


