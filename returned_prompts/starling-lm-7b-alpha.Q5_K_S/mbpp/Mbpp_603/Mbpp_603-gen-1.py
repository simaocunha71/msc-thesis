
def get_lucid(n: int) -> list:
  lucid_nums = [1, 2, 3, 5, 7]
  if n < 6:
    return lucid_nums
  i = 4
  while True:
    lucid_nums.append(sum(map(lambda x: x % 2, lucid_nums[i:i+5])))
    if lucid_nums[-1] > n:
      break
    i += 1
  return lucid_nums


