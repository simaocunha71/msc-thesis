def second_smallest(my_list):
  smallest = min(my_list)
  for i in my_list:
    if i != smallest:
      if i > smallest:
        return i
  return None