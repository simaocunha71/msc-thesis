def find_first_occurrence(sorted_array, target):
  for i in range(len(sorted_array)):
    if sorted_array[i] == target:
      return i
  return -1