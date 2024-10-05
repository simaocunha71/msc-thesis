    palindrome_suffix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            break

    prefix = string[:-len(palindrome_suffix)]
    return f'{prefix}{palindrome_suffix[::-1]}'


