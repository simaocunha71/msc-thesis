
def left_insertion(sorted_list, value):
  if value < sorted_list[0]:
    return 0
  elif value > sorted_list[-1]:
    return len(sorted_list)
  else:
    for i in range(len(sorted_list)):
      if sorted_list[i] < value:
        return i


