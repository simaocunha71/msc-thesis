def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170
print(dict_filter(d, n))

"""
In this function, we use a dictionary comprehension to create a new dictionary. The dictionary comprehension iterates over the items in the input dictionary, and if the value of an item is greater than or equal to n, it includes the item in the new dictionary.
"""
<jupyter_output>
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_text>
Exercise 8
<jupyter_code>
