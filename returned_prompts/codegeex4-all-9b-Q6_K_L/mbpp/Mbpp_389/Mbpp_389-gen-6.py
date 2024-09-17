def find_lucas(n: int) -> int:
  if n < 2:
    return n
  lucas_nums = [0, 1]
  for i in range(2, n+1):
    lucas_nums.append(lucas_nums[i-1] + lucas_nums[i-2])
  return lucas_nums[-1]