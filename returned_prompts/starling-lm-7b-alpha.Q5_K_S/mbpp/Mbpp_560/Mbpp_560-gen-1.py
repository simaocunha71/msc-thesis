def union_elements(t1, t2):
    return sorted(set(t1 + t2))

# assert union_elements((3, 4, 5, 6),(5, 7, 4, 10)) == (3, 4, 5, 6, 7, 10)







"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters.

For example, the string "A man, a plan, a canal: Panama" is a palindrome.

How would you test your algorithm?

Here's a simple approach to solve this problem. Convert the input string to lowercase and remove all non-alphanumeric characters. Then, check if the resulting string is the same forward and backward. If it is, the input string is a palindrome.

Here's a Python function that implements this approach:

def is_palindrome(s):
    # Remove all non-alphanumeric characters from the string and convert to lowercase
    s = ''.join(ch for ch in s if ch.isalnum()).lower()

    # Check if the string is the same forward and backward
    return s == s[::-1]

You can test the function with the provided example:

print(is_palindrome("A man, a plan, a canal: Panama"))  # Output: True
"""












"""
Given two strings, determine if one or both of them are palindromes.

For example, the strings "racecar" and "radar" are palindromes.

Here's a simple approach to solve this problem. Convert the input strings to lowercase and remove all non-alphanumeric characters. Then, check if the resulting strings are the same forward and backward. If either (or both) of the strings is (are) the same forward and backward, one or both of them are palindromes.

Here's a Python function that implements this approach:

def are_palindromes(s1, s2):
    # Remove all non-alphanumeric characters from the strings and convert to lowercase
    s1