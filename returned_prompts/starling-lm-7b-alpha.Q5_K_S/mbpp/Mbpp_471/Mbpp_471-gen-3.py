
def find_remainder(nums: list, mod: int) -> int:
  def mult(a, b):
    return (a * b) % mod
  return reduce(mult, nums)


