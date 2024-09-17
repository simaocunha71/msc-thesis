def next_smallest_palindrome(n: int) -> int:
  str_n = str(n)
  length = len(str_n)
  if length == 1:
    if n == 9:
      return 10
    else:
      return n + 1
  elif length == 2:
    if n == 99:
      return 100
    elif n == 98:
      return 101
    else:
      return int(str_n[0] + str(int(str_n[1]) + 1) + str_n[1])
  else:
    if n == 999:
      return 1000
    elif n == 998:
      return 1001
    elif n == 997:
      return int(str_n[0] + str(int(str_n[1]) + 1) + str_n[1] + str_n[2])
    else:
      return int(str_n[0] + str(int(str_n[1]) + 1) + str_n[1] + str_n[2])