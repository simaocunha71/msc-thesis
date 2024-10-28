from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']


In this solution, we use a list comprehension to iterate over the input list of strings. The condition `string.startswith(prefix)` is used to filter the strings that start with the given prefix. The list comprehension returns a new list of strings that pass the condition.
"""

# 12. Write a Python function to find the nth Fibonacci number.
def fibonacci(n: int) -> int:
    if n <= 0:
        raise ValueError("Input 0 or negative")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_nums = [0, 1]
        for _ in range(2, n):
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        return fib_nums[-1]


# 13. Write a Python function that checks if a string is a palindrome.
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# 14. Write a Python function that returns the number of occurrences of a substring in a given string.
def count_substring(string: str, substring: str) -> int:
    return string.count(substring)


# 15. Write a Python function that returns the number of vowels in a given string.
def count_vowels(s: str) -> int:
    return sum(s.count(vowel) for vowel in 'aeiouAEIOU')


# 16. Write a Python function that returns the number of words in a given string.
def count_words(s