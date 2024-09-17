def diff_even_odd(my_list):
  even = [x for x in my_list if x % 2 == 0]
  odd = [x for x in my_list if x % 2 != 0]
  return (even[0] - odd[0])