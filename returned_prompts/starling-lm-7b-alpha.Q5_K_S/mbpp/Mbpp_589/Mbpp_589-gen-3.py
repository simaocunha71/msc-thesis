
def perfect_squares(start: int, end: int) -> list:
  result = []
  for i in range(start, end+1):
    if i*i <= end:
      result.append(i*i)
  return result


