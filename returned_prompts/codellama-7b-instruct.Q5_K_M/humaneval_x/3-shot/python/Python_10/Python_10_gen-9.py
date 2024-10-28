    if is_palindrome(string):
        return string

    palindromes = []
    for i in range(len(string)):
        palindromes.append(string[i:])

    for palindrome in palindromes:
        if is_palindrome(palindrome):
            return string + palindrome[::-1]

    return string


