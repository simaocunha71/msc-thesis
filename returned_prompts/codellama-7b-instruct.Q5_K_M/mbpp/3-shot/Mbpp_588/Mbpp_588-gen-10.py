
def big_diff(my_list):
  largest = 0
  smallest = 0
  for i in my_list:
    if i > largest:
      largest = i
    if i < smallest or smallest == 0:
      smallest = i
  return largest - smallest


