
def max_sub_array_sum_repeated(nums: list, k: int, n: int) -> int:
  sums = []
  for i in range(k):
    sums.append(sum(nums))
  sums += sums[1:]
  return max(sums[:n])


