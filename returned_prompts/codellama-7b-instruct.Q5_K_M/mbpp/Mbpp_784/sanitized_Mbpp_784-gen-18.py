def mul_even_odd(my_list):
  product = 1
  for i in my_list:
    if i%2==0:
      product *= i
    else:
      product *= i
  return product