
def largest_subset(nums: list) -> int:
  def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

  def divisible(a, b):
    return a % b == 0

  nums.sort()
  i = 0
  while i < len(nums):
    j = i + 1
    while j < len(nums) and divisible(nums[i], nums[j]):
      j += 1
    i = j
  return i + 1


