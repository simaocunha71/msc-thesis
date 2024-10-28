    palindrome_postfix = ''

    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindrome_postfix = string[i:]
            break

    return string + palindrome_postfix[::-1]


