
def diff_even_odd(my_list):
  even = next((x for x in my_list if x % 2 == 0), None)
  odd = next((x for x in my_list if x % 2 != 0), None)
  return abs(even - odd)


