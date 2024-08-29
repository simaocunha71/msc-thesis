def sort_sublists(lst):
    return [sorted(lst) for lst in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""
Explanation:
The function 'sort_sublists' takes a list of lists as an argument. 
It uses list comprehension to iterate over each sublist in the given list. 
For each sublist, it uses the built-in 'sorted' function to sort the elements in ascending order and returns a new sorted list.
Finally, it returns a new list of the sorted sublists.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
Q2. Write a Python function to check whether a given string is a palindrome or not. Return True if it is a palindrome and False otherwise. A string is said to be a palindrome if the reverse of the string is the same as the string. The function should be case-insensitive.
<jupyter_code>
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome('Racecar'))
print(is_palindrome('Python'))
<jupyter_output>
True
False
<jupyter_text>
Q3. Write a Python function that takes a string as input and returns the number of vowels in the string. The function should be case-insensitive.
<jupyter_code>
def count_vowels(s):
    s = s.lower()
    return sum(map(s.count, "aeiou"))

print(count_vowels('Hello World'))
<jupyter_output>
3
<jupyter_text>
Q4. Write a Python function that takes a list of integers as input and returns a new list with the squares of the integers.
<jupyter_code>
def square_integers(lst):
    return [i**2 for i in