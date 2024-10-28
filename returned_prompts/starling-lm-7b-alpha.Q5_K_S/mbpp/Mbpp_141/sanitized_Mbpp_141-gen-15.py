def pancake_sort(nums:list):
  for i in range(len(nums)):
    max_index = i
    for j in range(i+1, len(nums)):
      if nums[j] > nums[max_index]:
        max_index = j
    nums[max_index], nums[i] = nums[i], nums[max_index]
    nums[:i+1] = reversed(nums[:i+1])
  return nums