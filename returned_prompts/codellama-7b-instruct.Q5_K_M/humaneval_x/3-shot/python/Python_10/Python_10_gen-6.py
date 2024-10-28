    prefix, suffix = string[:-1], string[1:]
    if is_palindrome(suffix):
        return string
    else:
        for i in range(1, len(suffix)):
            if is_palindrome(suffix[:i] + suffix[i + 1:]):
                return prefix + suffix[:i] + suffix[i:][::-1]


