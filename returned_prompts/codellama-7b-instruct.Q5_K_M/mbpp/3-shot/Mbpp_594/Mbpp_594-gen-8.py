
def diff_even_odd(my_list):
  first_even = next((x for x in my_list if x % 2 == 0), None)
  first_odd = next((x for x in my_list if x % 2 != 0), None)
  return first_even - first_odd


