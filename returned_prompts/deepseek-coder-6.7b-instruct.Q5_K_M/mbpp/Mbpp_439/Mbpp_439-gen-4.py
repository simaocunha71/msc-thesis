def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

print(multiple_to_single([11, 33, 50]))

#Alternate solution using list comprehension
def multiple_to_single(lst):
    return int(''.join([str(i) for i in lst]))

print(multiple_to_single([11, 33, 50]))

"""
Explanation:
The function works by converting each integer in the list to a string using the built-in map function and the str function. The map function applies the str function to every element in the list, and the result is a map object. The join method is then used on the map object to concatenate all the strings in the list into a single string. This single string is then converted back to an integer using the int function, and the integer is returned.
"""

#Alternate solution using f-string
def multiple_to_single(lst):
    return int(f"{lst[0]}{lst[1]}{lst[2]}")

print(multiple_to_single([11, 33, 50]))

"""
Explanation:
The function works by using f-string formatting to concatenate the integers in the list into a single string. The f-string is a string literal that is prefixed with 'f' or 'F'. The string inside the f-string is a format string, which is a mix of text and replacement fields. The replacement fields are expressions that are enclosed in curly braces {}. The values of the expressions are replaced with their string representations when the f-string is evaluated. In this case, the expressions are the elements of the list, which are replaced with their string representations to concatenate them into a single string. This single string is then converted back to an integer using the int function, and the integer is returned.
"""
<jupyter_output>
113350
113350
113350
<jupyter_text>
Question 2
<jupyter_code>
