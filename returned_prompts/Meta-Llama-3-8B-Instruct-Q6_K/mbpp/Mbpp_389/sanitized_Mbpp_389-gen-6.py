def find_lucas(n):
  if n == 1:
    return 2
  elif n == 2:
    return 1
  else:
    lucas_num = [2, 1]
    for i in range(2, n):
      lucas_num.append(lucas_num[i-1] + lucas_num[i-2])
    return lucas_num[-1]  # return the last element in the list