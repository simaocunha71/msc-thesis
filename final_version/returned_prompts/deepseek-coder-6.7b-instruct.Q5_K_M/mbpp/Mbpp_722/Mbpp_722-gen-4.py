def filter_data(students:dict, min_height:float, min_weight:float) -> dict:
    return {name: data for name, data in students.items() if data[0] >= min_height and data[1] >= min_weight}

# Test
print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
<jupyter_output>
{'Cierra Vega': (6.2, 70)}
<jupyter_text>
Question 3
<jupyter_code>
