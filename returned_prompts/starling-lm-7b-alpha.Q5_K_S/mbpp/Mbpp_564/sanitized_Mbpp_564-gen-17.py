def count_Pairs(nums:list,n:int)->int:
  length = len(nums)
  count = 0
  for i in range(length):
    for j in range(i+1,length):
      if nums[i] != nums[j]:
        count += 1
  return count