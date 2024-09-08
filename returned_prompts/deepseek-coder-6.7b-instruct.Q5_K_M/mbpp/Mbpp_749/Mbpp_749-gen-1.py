
def sort_numeric_strings(lst):
    return sorted(int(i) for i in lst)

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))

"""
In the function "sort_numeric_strings", we are using a generator expression that converts each string in the list to an integer, and then sorts them. This is done using the built-in sorted function, which returns a new list containing all items from the original list in ascending order.
"""
<jupyter_output>
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<jupyter_text>
3. Write a Python function that accepts a string and returns a list of all substrings of that string. The order of the substrings in the returned list does not matter, but each substring must be unique.
<jupyter_code>
def all_substrings(input_string):
    length = len(input_string)
    return [input_string[i: j] for i in range(length) for j in range(i + 1, length + 1)]

print(all_substrings("abc"))
<jupyter_output>
['a', 'ab', 'abc', 'abcd', 'b', 'bc', 'c']
<jupyter_text>
4. Write a Python function to check if a string is a palindrome or not. A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
<jupyter_code>
def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
<jupyter_output>
True
False
<jupyter_text>
5. Write a