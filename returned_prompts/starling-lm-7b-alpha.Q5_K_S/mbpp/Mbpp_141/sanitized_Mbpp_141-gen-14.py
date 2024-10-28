def pancake_sort(nums):
  for i in range(len(nums)):
    max_ele = max(nums[i:])
    index = nums[i:].index(max_ele)
    nums.append(nums.pop(i + index))
  return nums[i + 1:]