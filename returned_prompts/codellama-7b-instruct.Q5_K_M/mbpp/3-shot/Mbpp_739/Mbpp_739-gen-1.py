
def find_Index(n: int) -> int:
  smallest_triangular_number = 1
  length_of_smallest_triangular_number = 1
  index = 1
  while length_of_smallest_triangular_number != n:
    smallest_triangular_number += 1
    length_of_smallest_triangular_number = len(str(smallest_triangular_number))
    index += 1
  return index


