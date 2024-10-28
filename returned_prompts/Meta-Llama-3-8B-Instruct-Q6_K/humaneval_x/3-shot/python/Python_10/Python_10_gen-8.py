    def is_palindrome(s):
        return s == s[::-1]

    def longest_palindromic_suffix(s):
        for i in range(len(s)):
            if is_palindrome(s[i:]):
                return s[i:]

    def make_palindrome(s):
        palindromic_suffix = longest_palindromic_suffix(s)
        return s + s[::-1].replace(palindromic_suffix[::-1], '')

    return make_palindrome


