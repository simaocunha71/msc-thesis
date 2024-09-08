def dict_filter(dic, n):
    return {k: v for k, v in dic.items() if v >= n}

# Test
dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170
print(dict_filter(dic, n))

# Output: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

"""
Explanation:
The function `dict_filter` uses a dictionary comprehension to create a new dictionary that includes only the entries where the value is greater than or equal to n. The if condition inside the dictionary comprehension ensures that only entries with values greater than or equal to n are included in the new dictionary.
"""

