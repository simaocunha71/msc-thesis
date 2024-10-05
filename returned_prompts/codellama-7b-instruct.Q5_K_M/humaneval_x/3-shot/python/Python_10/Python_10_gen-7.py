    palindrome_suffix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            break

    return string + palindrome_suffix[::-1]


