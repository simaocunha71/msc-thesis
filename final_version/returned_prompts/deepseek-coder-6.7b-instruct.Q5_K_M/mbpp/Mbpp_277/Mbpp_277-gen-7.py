def dict_filter(d, n):
    return {key: value for key, value in d.items() if value >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))


"""
Explanation:
In the function, we use dictionary comprehension to create a new dictionary. The expression inside the brackets is a conditional statement that checks if the value is greater than or equal to n. Only the entries that satisfy this condition are included in the new dictionary.
"""

# Alternatively, you can use the built-in `filter()` function:

def dict_filter(d, n):
    return dict(filter(lambda x: x[1] >= n, d.items()))

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))

"""
Explanation:
The `filter()` function creates a list of elements for which a function returns true. The lambda function checks if the value (x[1]) is greater than or equal to n. The `dict()` function converts the filtered list of tuples back into a dictionary.
"""
<jupyter_output>
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_text>
3. Write a function that converts a list of integers into a single integer. For instance, if the input list is [1, 2, 3], the output should be 123.
<jupyter_code>
def convert_to_int(lst):
    return int(''.join(map(str, lst)))

print(convert_to_int([1, 2, 