    palindromic_postfix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            palindromic_postfix = string[:i]
            break

    prefix = string[:len(string) - len(palindromic_postfix)]
    return prefix + palindromic_postfix[::-1]
