from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Tests
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

In this solution, we use a list comprehension to create a new list that only includes the strings that contain the given substring. This is done using the 'in' operator, which checks if a string contains the specified substring. The function then returns this new list.

The time complexity of this solution is O(n*m) where n is the length of the input list and m is the length of the substring. This is because for each string in the list, we check if it contains the substring.

The space complexity is O(k) where k is the number of strings that contain the substring. This is because we create a new list that contains these strings.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2 Write a function that checks if a given string is a palindrome.A palindrome is a word, number, phrase, or other sequences of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.Examples:is_palindrome("level") => Trueis_palindrome("A man, a plan, a canal: Panama") => Trueis_palindrome("No 'x' in Nixon") => Trueis_palindrome("asd") => False
<jupyter_code>
