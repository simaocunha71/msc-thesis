
def mul_even_odd(lst):
  even = [i for i in lst if i%2 == 0]
  odd = [i for i in lst if i%2 != 0]
  return even[0] * odd[0]


