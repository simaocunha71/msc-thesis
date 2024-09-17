def next_smallest_palindrome(n: int) -> int:
  temp = str(n)
  if len(temp) == 1:
    return int(temp) + 1
  elif len(temp) == 2:
    if temp[0] == temp[1]:
      return int(temp) + 1
    else:
      return int(temp[0] + str(int(temp[1]) + 1))
  else:
    if temp[0] == temp[1]:
      return int(temp) + 1
    else:
      return int(temp[0] + str(int(temp[1]) + 1))