
def diff_even_odd(lst):
  even = next((x for x in lst if x % 2 == 0), None)
  odd = next((x for x in lst if x % 2 != 0), None)
  return even - odd if even and odd else None

