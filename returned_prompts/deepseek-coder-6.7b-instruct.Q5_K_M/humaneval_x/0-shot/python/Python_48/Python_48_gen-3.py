
    return text == text[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


# Testing the function
print(is_palindrome(''))  # True
print(is_palindrome('aba'))  # True
print(is_palindrome('aaaaa'))  # True
print(is_palindrome('zbcd'))  # False
print(is_palindrome('a'))  # True
print(is_palindrome('abc'))  # False
print(is_palindrome('abcba'))  # True
print(is_palindrome('abcdcba'))  # False
print(is_palindrome('wasitacaroracatisaw'))  # True
print(is_palindrome('z'))  # True
print(is_palindrome('zz'))  # True
print(is_palindrome('zzz'))  # True
print(is_palindrome('zozzo'))  # False
print(is_palindrome('azbcbaz'))  # True
print(is_palindrome('wasitacaroracatisaw'))  # True
print(is_palindrome('azbcbaz'))  # True
print(is_palindrome('abcdefgfedcba'))  # True
print(is_palindrome('aabaa'))  # True
print(is_palindrome('aaaa'))  # True
print(is_palindrome('aaa'))  # True
print(is_palindrome('aa'))  # True
print(is_palindrome('a'))  # True
print(is_palindrome('aaaaaa'))  # True
print(is_palindrome('azbcbaz'))  # True
print(is_palindrome('abcdefghgfedcba'))  # True
print(is_palindrome('abcdefghghfedcba'))  # True
print(is_palindrome('abcdefghhgfedcba'))  # True
print(is_palindrome('abcdefghihgfedcba'))  #