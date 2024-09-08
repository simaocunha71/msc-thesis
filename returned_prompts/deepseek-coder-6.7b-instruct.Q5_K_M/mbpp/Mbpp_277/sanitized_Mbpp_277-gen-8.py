def dict_filter(dic, n):
    return {k: v for k, v in dic.items() if v >= n}
dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170