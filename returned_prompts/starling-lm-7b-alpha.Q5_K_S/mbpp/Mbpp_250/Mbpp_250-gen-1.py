
def count_X(tup: tuple, elem: int) -> int:
  count = 0
  for i in tup:
    if i == elem:
      count+=1
  return count


