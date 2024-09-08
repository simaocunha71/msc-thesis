def dict_filter(d, n):
    return {k: v for k, v in d.items() if v >= n}
d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170