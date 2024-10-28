
def left_insertion(sorted_list:list,target:int)->int:
  left_index = -1
  for i in range(len(sorted_list)):
    if target > sorted_list[i]:
      left_index = i
    else:
      break
  return left_index


