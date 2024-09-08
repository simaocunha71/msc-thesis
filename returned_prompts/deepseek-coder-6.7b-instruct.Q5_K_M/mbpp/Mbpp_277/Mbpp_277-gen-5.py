def dict_filter(dic, n):
    return {key: value for key, value in dic.items() if value >= n}

print(dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170))

