def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))

"""
This function uses a list comprehension to create a new list where each sublist is sorted. The sorted function is used to sort each sublist.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
3. Write a Python function named `reverse_string` that takes a string as input and returns the reversed string.
<jupyter_code>
def reverse_string(string):
    return string[::-1]

print(reverse_string("Hello, World!"))
<jupyter_output>
¡dlroW ,olleH
<jupyter_text>
4. Write a Python function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise.
<jupyter_code>
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
<jupyter_output>
True
False
<jupyter_text>
5. Write a Python function named `count_vowels` that takes a string as input and returns the number of vowels in the string.
<jupyter_code>
def count_vowels(string):
    return sum(1 for char in string if char.lower() in 'aeiou')

print(count_vowels("Hello, World!"))
<jupyter_output>
3
<jupyter_text>
6. Write a Python function named `remove_duplicates` that takes a list as input and returns a new list with duplicates removed.
<jupyter_code>
def remove_duplicates(lst):
    return list(set(