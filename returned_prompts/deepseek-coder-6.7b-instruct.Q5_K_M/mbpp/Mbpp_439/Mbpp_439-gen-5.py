def multiple_to_single(lst):
    return int(''.join(map(str, lst)))

print(multiple_to_single([11, 33, 50]))

#output: 113350

Explanation:
The function takes a list of integers as an input. It converts each integer in the list to a string using the map() function. The map() function applies the str() function to every item in the list. Then it joins all the strings into one big string using the join() function. Finally it converts this string back to an integer using the int() function.
<jupyter_output>
<empty_output>
<jupyter_text>
