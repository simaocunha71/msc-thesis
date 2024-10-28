def find_star_num(n: int) -> int:
  star_nums = []
  for i in range(n):
    star_nums.append(i + 1)
    if i % 2 == 0:
      star_nums[i] *= 2
  return sum(star_nums)