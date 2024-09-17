def bell_number(n: int) -> int:
  bell_nums = [1, 1]
  for i in range(2, n+1):
    bell_nums.append(sum(bell_nums[:i]))
  return bell_nums[-1]