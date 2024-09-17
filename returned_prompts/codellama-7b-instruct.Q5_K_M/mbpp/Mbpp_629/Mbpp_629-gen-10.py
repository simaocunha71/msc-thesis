
def Split(my_list):
  even_nums = []
  for num in my_list:
    if num % 2 == 0:
      even_nums.append(num)
  return even_nums


