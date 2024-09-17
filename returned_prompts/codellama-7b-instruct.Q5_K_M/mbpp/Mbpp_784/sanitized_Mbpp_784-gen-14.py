def mul_even_odd(my_list):
  ev = 1
  od = 1
  for i in my_list:
    if i % 2 == 0:
      ev *= i
    else:
      od *= i
  return ev * od