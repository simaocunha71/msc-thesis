def sum_in_range(l: int, r: int) -> int:
  if l % 2 == 0 and r % 2 == 0:
    return (r - l) // 2
  elif l % 2 != 0 and r % 2 != 0:
    return ((r + l) // 2) * (r - l + 1)
  elif l % 2 != 0 and r % 2 == 0:
    return ((r + l) // 2) * (r - l + 1) - (r // 2)
  elif l % 2 == 0 and r % 2 != 0:
    return ((r + l) // 2) * (r - l + 1) - (l + 1) // 2