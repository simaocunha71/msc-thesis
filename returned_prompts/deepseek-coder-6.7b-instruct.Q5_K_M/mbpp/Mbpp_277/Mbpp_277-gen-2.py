def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))

"""
Explanation:
The function `dict_filter` takes in a dictionary `d` and an integer `n`. It then uses a dictionary comprehension to create a new dictionary that includes only the entries from `d` where the value is greater than or equal to `n`. This is done by checking each key-value pair in `d` and including it in the new dictionary only if the value is greater than or equal to `n`. The function then returns this new dictionary.
"""
<jupyter_output>
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_text>
Q2:
<jupyter_code>
