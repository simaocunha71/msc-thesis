def remove_odd(my_list):
  new_list = []
  for num in my_list:
    if num % 2 == 0:
      new_list.append(num)
  return new_list