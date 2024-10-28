def diff_even_odd(my_list):
  ev = [x for x in my_list if x % 2 == 0]
  od = [x for x in my_list if x % 2 != 0]
  return od[0] - ev[0]