"""
The input is given as - a dictionary with a student name as a key and a tuple of float (student_height, student_weight) as a value, - minimal height, - minimal weight. Write a function to filter students that have height and weight above the minimum.
assert filter_data({'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)},6.0,70)=={'Cierra Vega': (6.2, 70)}
"""

def filter_data(data, min_height, min_weight):
    filter = []
    for student in data:
        height, weight = student['student']
        if height >= min_height and weight >= min_weight:
            filter.append({'name': student['name'], 'student': (height, weight)})
    return(filter)


"""

Write a program that prints the names of students with heights above 168 cm, but whose weights are less than 70 kg. Also, print the name of each student with both of these criteria met.
assert filter_data({'Adrien Mcbride': (169, 72), 'Aurora Vega': (165, 64)},168,70)=={'Adrien Mcbride': (169, 72)}
filter_data([],168,70)
"""