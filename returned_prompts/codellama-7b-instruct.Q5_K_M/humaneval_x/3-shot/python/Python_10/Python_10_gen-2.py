    palindrome = ''

    for i in range(len(string)):
        if is_palindrome(string[::-1]):
            palindrome = string[::-1]
            break
        else:
            palindrome = string[i:]

    return palindrome + string[:i:-1]


