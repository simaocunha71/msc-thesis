def shell_sort(arr):
  sublist_count = len(arr) // 2
  while sublist_count > 0:
    for start_index in range(sublist_count):
      gap_insertion_sort(arr, start_index, sublist_count)
    sublist_count //= 2
  return arr