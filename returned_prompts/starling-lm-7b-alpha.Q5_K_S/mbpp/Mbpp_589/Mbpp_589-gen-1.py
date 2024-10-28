
def perfect_squares(lower_limit: int, upper_limit: int) -> list:
  perfect_squares_list = []
  for i in range(lower_limit, upper_limit+1):
    if i == int(i**0.5) ** 2:
      perfect_squares_list.append(i)
  return perfect_squares_list


