
def count_Substrings(nums):
  count = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if sum([int(nums[k]) for k in range(i, j + 1)]) == j - i + 1:
        count += 1
  return count


