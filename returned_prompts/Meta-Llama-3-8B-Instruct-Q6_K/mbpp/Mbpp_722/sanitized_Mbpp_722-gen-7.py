def filter_data(students, min_height, min_weight):
  return {name: (height, weight) for name, (height, weight) in students.items() if height > min_height and weight > min_weight}
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 70