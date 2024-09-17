
def diff_even_odd(nums):
  first_even = next((x for x in nums if x % 2 == 0), None)
  first_odd = next((x for x in nums if x % 2 != 0), None)
  return first_even - first_odd if first_even and first_odd else None


