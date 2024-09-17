
def mul_even_odd(lst):
  evens = [i for i in lst if i % 2 == 0]
  odds = [i for i in lst if i % 2 != 0]
  return evens[0] * odds[0]


