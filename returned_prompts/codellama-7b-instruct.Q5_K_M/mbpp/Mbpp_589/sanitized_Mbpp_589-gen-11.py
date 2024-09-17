def perfect_squares(start: int, end: int) -> list:
  perfect_squares_list = []
  for i in range(start, end + 1):
    if i**0.5 == int(i**0.5):
      perfect_squares_list.append(i)
  return perfect_squares_list