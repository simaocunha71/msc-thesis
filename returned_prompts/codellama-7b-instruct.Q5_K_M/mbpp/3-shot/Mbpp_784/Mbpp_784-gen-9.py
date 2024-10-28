
def mul_even_odd(my_list):
  even_prod = 1
  odd_prod = 1
  for i in my_list:
    if i % 2 == 0:
      even_prod *= i
    else:
      odd_prod *= i
  return even_prod * odd_prod


