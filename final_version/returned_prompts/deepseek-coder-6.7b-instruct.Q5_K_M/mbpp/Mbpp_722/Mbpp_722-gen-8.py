
def filter_data(student_data, min_height, min_weight):
    return {student: data for student, data in student_data.items() if data[0] >= min_height and data[1] >= min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))
<jupyter_output>
{'Cierra Vega': (6.2, 70)}
<jupyter_text>
Question 2
<jupyter_code>
