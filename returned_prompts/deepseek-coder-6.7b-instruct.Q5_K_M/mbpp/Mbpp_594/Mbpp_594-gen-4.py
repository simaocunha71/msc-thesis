
def diff_even_odd(lst):
  even_num = next((x for x in lst if x % 2 == 0), None)
  odd_num = next((x for x in lst if x % 2 != 0), None)
  if even_num is None or odd_num is None:
    return None
  return even_num - odd_num

