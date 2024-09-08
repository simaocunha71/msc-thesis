
def filter_data(dict_of_students, min_height, min_weight):
    return {name: (height, weight) for name, (height, weight) in dict_of_students.items() if height >= min_height and weight >= min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
<jupyter_output>
{'Cierra Vega': (6.2, 70)}
<jupyter_text>
Question 2
<jupyter_code>
