def smallest_num(my_list):
  smallest = my_list[0]
  for i in my_list:
    if i < smallest:
      smallest = i
  return smallest