def diff_even_odd(my_list):
  even_num = next((x for x in my_list if x % 2 == 0), None)
  odd_num = next((x for x in my_list if x % 2 != 0), None)
  return even_num - odd_num