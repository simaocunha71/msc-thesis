
def filter_data(students_data, min_height, min_weight):
    return {name: data for name, data in students_data.items() if data[0] >= min_height and data[1] >= min_weight}

print(filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70))

# Expected output: {'Cierra Vega': (6.2, 70)}

"""
Explanation:
The function filter_data takes a dictionary, min_height and min_weight as inputs. It uses dictionary comprehension to go through each key-value pair in the dictionary. If the height and weight of a student is greater or equal to min_height and min_weight respectively, it includes the student in the output dictionary.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
"""
