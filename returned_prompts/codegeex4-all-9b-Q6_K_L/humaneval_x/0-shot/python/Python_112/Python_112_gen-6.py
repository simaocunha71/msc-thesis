def reverse_delete(s, c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """
    return (''.join([i for i in s if i not in c]), s == s[::-1])

print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)
print(reverse_delete("abc", "a"))  # ('bc', False)
print(reverse_delete("abcdcba", "a"))  # ('bcdc', True)
print(reverse_delete("a", "a"))  # ('', False)
print(reverse_delete("a", "b"))  # ('a', False)
print(reverse_delete("abba", "ab"))  # ('', True)
print(reverse_delete("aba", "ab"))  # ('', True)
print(reverse_delete("ababab", "ab"))  # ('', True)
print(reverse_delete("a", "b"))  # ('a', False)
print(reverse_delete("abcd", "a"))  # ('bcd', False)
print(reverse_delete("ab", "a"))  # ('b', False)
print(reverse_delete("a", "b"))  # ('a', False)
print(reverse_delete("ab", "b"))  # ('a', False)
print(reverse_delete("abc", "b"))  # ('ac', False)
print(reverse_delete("abc", "c"))  # ('ab', False)
print(reverse_delete("abc", "d"))  # ('abc', False)
print(reverse_delete("abc", "a"))  # ('bc', False)
print(reverse_delete("abc", "abc"))  # ('', True)
print(reverse_delete("abc",