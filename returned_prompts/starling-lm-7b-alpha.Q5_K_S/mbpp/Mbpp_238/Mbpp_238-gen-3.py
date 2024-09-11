def number_of_substrings(s):
    length = len(s)
    return (length * (length + 1)) // 2

number_of_substrings("abc")

# This function works by calculating the total number of substrings in the string. A substring is considered non-empty if its length is greater than 0. A substring can be of any length, even if it's only one character long. This means that every character in the string is part of a substring.

# To calculate the total number of substrings in a string, we can use the formula n * (n + 1) / 2, where n is the length of the string. This formula works because every substring of length i in a string of length n is also a substring of length i - 1 in a string of length n - 1.

# So, for example, in the string "abc", there are 6 substrings: "a", "ab", "abc", "b", "bc", and "c". The function number_of_substrings("abc") returns 6, as expected.

"""
The above code works by calculating the total number of substrings in a string using the formula n * (n + 1) / 2, where n is the length of the string. This formula works because every substring of length i in a string of length n is also a substring of length i - 1 in a string of length n - 1.

For example, in the string "abc", there are 6 substrings: "a", "ab", "abc", "b", "bc", and "c". The function number_of_substrings("abc") returns 6, as expected.
"""

"""
The above code works by calculating the total number of substrings in a string using the formula n * (n + 1) / 2, where n is the length of the string. This formula works because every substring of length i in a string of length n is also a substring of length i - 1 in a string of length n - 1.

For example, in the string "abc", there are 6 substrings: "a", "ab", "abc", "b", "bc", and "c". The function number_of_