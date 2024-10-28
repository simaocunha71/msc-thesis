
def centered_hexagonal_number(n: int) -> int:
  hexagon_nums = [1]
  for i in range(1, n):
    hexagon_nums.append(hexagon_nums[i-1] + (4 * i))
  return hexagon_nums[n-1]


