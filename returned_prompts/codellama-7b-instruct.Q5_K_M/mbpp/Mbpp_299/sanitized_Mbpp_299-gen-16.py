def max_aggregate(students_grades: list) -> tuple:
  return max(students_grades, key=lambda x: x[1])