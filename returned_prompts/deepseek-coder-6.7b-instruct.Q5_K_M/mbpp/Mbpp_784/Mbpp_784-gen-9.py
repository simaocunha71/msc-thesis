
def mul_even_odd(lst):
  even_lst = [i for i in lst if i%2 == 0]
  odd_lst = [i for i in lst if i%2 != 0]
  return even_lst[0] * odd_lst[0]


