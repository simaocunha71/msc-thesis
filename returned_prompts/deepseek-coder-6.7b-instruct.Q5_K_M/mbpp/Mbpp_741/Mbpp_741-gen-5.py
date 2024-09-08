def all_Characters_Same(string):
    return string == string[0] * len(string)

print(all_Characters_Same("python"))

#Output: False

"""
The function works by comparing the input string to a new string created by repeating the first character of the input string as many times as there are characters in the input string. If the input string is the same as this new string, the function returns True; otherwise, it returns False.
"""

#Example 2:
assert all_Characters_Same("ooo") == True

#Output: True

#Example 3:
assert all_Characters_Same("p") == True

#Output: True

#Example 4:
assert all_Characters_Same("") == True

#Output: True
<jupyter_output>
False
True
True
True
True
<jupyter_text>
Exercise 2:Write a Python function that accepts a string and returns the count of non-space characters in the string.assert count_non_space_characters("Python") == 6assert count_non_space_characters("Programming in Python") == 18assert count_non_space_characters("   ") == 0
<jupyter_code>
def count_non_space_characters(string):
    return len(string.replace(" ", ""))

print(count_non_space_characters("Python"))
print(count_non_space_characters("Programming in Python"))
print(count_non_space_characters("   "))
<jupyter_output>
6
18
0
<jupyter_text>
Exercise 3:Write a Python function that takes a string as input and returns a new string with all the words reversed. Note that words are separated by spaces.assert reverse_words("Hello World") == "World Hello"assert reverse_words("Python Programming") == "Programming Python"
<jupyter_code>
def reverse_words(string):
    return " ".join(string.split()[::-1])

print(reverse_words("Hello World"))
print(reverse_words("Python Programming