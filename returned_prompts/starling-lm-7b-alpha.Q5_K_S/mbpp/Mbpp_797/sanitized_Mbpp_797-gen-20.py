def sum_in_range(l: int, r: int):
  if l % 2 == 0 and r % 2 == 0:
    return (r-l)//2
  elif l % 2 == 0 and r % 2 != 0:
    return (r-l)//2 + r
  elif l % 2 != 0 and r % 2 == 0:
    return (r-l)//2 + l
  else:
    return (r-l)//2 + l + r