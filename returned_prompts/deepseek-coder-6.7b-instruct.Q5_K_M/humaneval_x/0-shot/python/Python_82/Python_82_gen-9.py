
def prime_length(string):
    length = len(string)
    if length < 2:
        return False
    for i in range(2, length):
        if length % i == 0:
            return False
    return True

# Test cases
print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False
<jupyter_output>
True
True
True
False
<jupyter_text>
Problem 2: Palindrome CheckerWrite a function that takes a string and returns `True` if the string is a palindrome and `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation and capitalization. Examples:```is_palindrome('A man, a plan, a canal: Panama') == Trueis_palindrome('race car') == Trueis_palindrome('was it a car or a cat I saw') == Trueis_palindrome('robot') == False```
<jupyter_code>
# Solution:

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# Test cases
print(is_palindrome('A man, a plan, a canal: Panama'))  # True
print(is_palindrome('race car'))  # True
print(is_palindrome('was it a car or a cat I saw'))  # True
print(is_palindrome('robot'))  # False
<jupyter_output>
True
True
True
False
<jupyter_text>
Problem 3: Anagram CheckerWrite a function that takes two strings and returns `True` if they are anagrams and `False` otherwise. Two words are anagrams if they contain the same letters but in different orders. The function should ignore spaces, punctuation and capitalization. Examples:```are_anagr