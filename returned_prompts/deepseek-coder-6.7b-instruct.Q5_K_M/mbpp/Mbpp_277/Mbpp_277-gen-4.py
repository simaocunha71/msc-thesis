def dict_filter(dic,n):
    return {k: v for k, v in dic.items() if v >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))


"""
The function dict_filter filters the dictionary dic by returning a new dictionary that only contains the entries where the value is greater or equal to n. This is achieved by using a dictionary comprehension. The dictionary comprehension iterates over the key-value pairs in the dictionary dic and includes them in the new dictionary only if the value is greater or equal to n.
"""

"""
Here is a breakdown of the function:
- The function dict_filter takes two parameters, a dictionary dic and an integer n.
- It returns a new dictionary that includes only the key-value pairs from the original dictionary dic where the value is greater or equal to n.
- This is done using a dictionary comprehension, which is a compact way of creating a new dictionary from an existing one.
- The dictionary comprehension iterates over the key-value pairs in the original dictionary dic.
- For each pair, it includes the pair in the new dictionary if the value is greater or equal to n.
"""

"""
In the given example, the function is called with a dictionary {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190} and n is 170. The function returns a new dictionary that includes only the key-value pairs where the value is greater or equal to 170. The resulting dictionary is {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}, which matches the expected output.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
