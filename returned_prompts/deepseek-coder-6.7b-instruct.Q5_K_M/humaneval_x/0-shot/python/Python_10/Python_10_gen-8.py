

    def longest_palindromic_postfix(string: str) -> str:
        """ Find the longest palindromic postfix of a supplied string. """
        for i in range(len(string), -1, -1):
            if is_palindrome(string[i:]):
                return string[i:]
        return ''

    palindrome = longest_palindromic_postfix(string)
    prefix = string[:len(string) - len(palindrome)]

    return string + prefix[::-1]


# Tests:
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
print(make_palindrome('tac'))  # 'tactac'
print(make_palindrome('b'))  # 'b'
print(make_palindrome('bb'))  # 'bb'
print(make_palindrome('abc'))  # 'abcba'
print(make_palindrome('abcd'))  # 'abcdcba'
print(make_palindrome('amanaplanacanalpanama'))  # 'amanaplanacanalpanama'
print(make_palindrome('amanaplanacanalpandulum'))  # 'amanaplanacanalpanadulumpandulum'

The algorithm first finds the longest palindromic postfix of the supplied string. If the string is already a palindrome, it returns the string itself. Then it finds the prefix of the string that comes before the palindromic postfix and appends to the string the reverse of this prefix.

The time complexity of the algorithm is O(n^2) due to the usage of the is_palindrome function in the longest_palindromic_postfix function. The space complexity is O(n) for storing the input string and the auxiliary strings.

Note that this algorithm works well for short strings, but it can be slow for long strings due to the quadratic time complexity.
"""

# ---------------------
# SOLUTION: KMP (Knuth–Morris–