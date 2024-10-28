def find_tuples(nums:list,k:int) -> list:
  result = []
  for i in nums:
    if all(j%k == 0 for j in i):
      result.append(i)
  return result