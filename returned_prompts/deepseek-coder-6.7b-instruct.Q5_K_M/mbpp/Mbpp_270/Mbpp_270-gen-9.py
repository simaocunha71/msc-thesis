
def sum_even_and_even_index(lst):
  return sum(elm for idx, elm in enumerate(lst) if idx % 2 == 0 and elm % 2 == 0)


