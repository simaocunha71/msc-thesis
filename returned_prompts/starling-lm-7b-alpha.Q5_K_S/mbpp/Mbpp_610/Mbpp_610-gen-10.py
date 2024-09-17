
def remove_kth_element(nums:list,k:int)->list:
  new_list = []
  for i in range(len(nums)):
    if i != k:
      new_list.append(nums[i])
  return new_list


