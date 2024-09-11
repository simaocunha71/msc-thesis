def filter_data(d, h_min, w_min):
    res = {}
    for k, v in d.items():
        if v[0] > h_min and v[1] > w_min:
            res[k] = v
    return res

filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)
"""
{
    'Cierra Vega': (6.2, 70)
}
"""

# Another approach
def filter_data2(d, h_min, w_min):
    return {k: v for k, v in d.items() if v[0] > h_min and v[1] > w_min}

filter_data2({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)
"""
{
    'Cierra Vega': (6.2, 70)
}
"""

# Another approach
def filter_data3(d, h_min, w_min):
    return {k: v for k, v in d.items() if v[0] > h_min and v[1] > w_min}

filter_data3({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)
"""
{
    'Cierra Vega': (6.2, 70)
}
"""

# Another approach
def filter_data4(d, h_min, w_min):
    res = {}
    for k, v in d