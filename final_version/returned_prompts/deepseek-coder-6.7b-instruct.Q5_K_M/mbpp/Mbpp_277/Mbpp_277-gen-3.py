def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))
<jupyter_output>
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
<jupyter_text>
