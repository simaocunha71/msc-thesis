
def mul_even_odd(lst: list):
  even_num = next((x for x in lst if x % 2 == 0), None)
  odd_num = next((x for x in lst if x % 2 != 0), None)
  return even_num * odd_num if even_num and odd_num else None


