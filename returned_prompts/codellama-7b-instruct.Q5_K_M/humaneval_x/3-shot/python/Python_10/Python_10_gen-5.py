    if is_palindrome(string):
        return string

    # Longest postfix of supplied string that is a palindrome
    palindrome = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindrome = string[i:]

    # Reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:-len(palindrome)]
    reversed_prefix = prefix[::-1]

    return f'{string}{reversed_prefix}'


