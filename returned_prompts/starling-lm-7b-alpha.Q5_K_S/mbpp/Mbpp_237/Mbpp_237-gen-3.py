
def check_occurences(nums: list) -> dict:
  counter = {}
  for num in nums:
    if num in counter:
      counter[num] += 1
    else:
      counter[num] = 1
  return counter


