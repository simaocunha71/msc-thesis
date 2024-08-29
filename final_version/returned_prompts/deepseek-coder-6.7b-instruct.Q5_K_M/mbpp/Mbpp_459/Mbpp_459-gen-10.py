def remove_uppercase(s):
    return "".join([c for c in s if not c.isupper()])

print(remove_uppercase('cAstyoUrFavoRitETVshoWs'))  # Output: 'cstyoravoitshos'

"""
Explanation:
The function uses a list comprehension to iterate over each character in the string. 
If the character is not uppercase (i.e., `c.isupper()` is `False`), it's included in the list.
The `join` method is used to concatenate all the characters back into a single string.
"""

# 2. Implement a function to remove all the vowels from a given string.

