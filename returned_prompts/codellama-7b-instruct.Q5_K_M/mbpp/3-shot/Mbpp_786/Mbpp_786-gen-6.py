
def right_insertion(sorted_list, value):
  index = 0
  while index < len(sorted_list) and sorted_list[index] < value:
    index += 1
  return index


