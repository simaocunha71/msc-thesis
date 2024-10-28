def pancake_sort(nums: list) -> list:
  while len(nums) > 1:
    max_el = max(nums[:len(nums)//2])
    index = nums.index(max_el)
    nums.insert(0,nums.pop(index+len(nums)//2))
  return nums