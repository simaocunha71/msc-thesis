    postfix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            postfix = string[i:]
            break
    prefix = ''
    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[:i]):
            prefix = string[:i]
            break
    return postfix + prefix[::-1]
