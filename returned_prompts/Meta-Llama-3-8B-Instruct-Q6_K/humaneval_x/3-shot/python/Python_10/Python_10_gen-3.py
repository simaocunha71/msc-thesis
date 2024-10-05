    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def longest_palindromic_suffix(s: str) -> str:
        i = 0
        while i < len(s) and is_palindrome(s[i:]):
            i += 1
        return s[:i]

    def make_palindrome(s: str) -> str:
        suffix = longest_palindromic_suffix(s)
        prefix = s[:len(s) - len(suffix)]
        return suffix + prefix[::-1]

    return make_palindrome(string)  # or is_palindrome(string) to test the function
# test function
print(is_palindrome('catac'))  # True
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'


