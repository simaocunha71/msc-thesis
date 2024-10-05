    palindromic_suffix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            palindromic_suffix = string[i:]
            break

    palindromic_prefix = ''
    for i in range(len(string[:-1])):
        if is_palindrome(string[:-i]):
            palindromic_prefix = string[:-i]
            break

    palindrome = palindromic_suffix + palindromic_prefix[::-1]
    if palindrome[: len(string)] == string:
        return palindrome

    return string + palindrome


