def Split(my_list):
  even_numbers = []
  for num in my_list:
    if num % 2 == 0:
      even_numbers.append(num)
  return even_numbers