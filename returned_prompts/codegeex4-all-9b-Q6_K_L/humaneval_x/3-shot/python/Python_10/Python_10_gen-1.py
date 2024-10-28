    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    if is_palindrome(string):
        return string

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            prefix = string[:i]
            postfix = string[i:]
            return postfix + prefix[::-1]

    return string + string[::-1]


