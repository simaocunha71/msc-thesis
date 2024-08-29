def dict_filter(dic, n):
    return {k: v for k, v in dic.items() if v >= n}

# Test
dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170
print(dict_filter(dic, n))

# Output: {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_output>
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_text>
