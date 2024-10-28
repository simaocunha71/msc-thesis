def find_remainder(nums: list,n: int) -> int:
  def find_product(left,right):
    if left == right:
      return nums[left] % n
    res = 1
    for i in range(left, right+1):
      res = (res * nums[i]) % n
    return res
  return find_product(0, len(nums)-1)