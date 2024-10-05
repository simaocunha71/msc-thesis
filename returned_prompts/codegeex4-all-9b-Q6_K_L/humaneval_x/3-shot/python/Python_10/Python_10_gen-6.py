    def longest_palindromic_suffix(string):
        for i in range(len(string)):
            if string[i:] == string[i:][::-1]:
                return string[i:]
        return ''

    def reverse(string):
        return string[::-1]

    if is_palindrome(string):
        return string

    postfix = longest_palindromic_suffix(string)
    prefix = string[:-len(postfix)]
    return string + reverse(prefix)

