def is_Sub_Array(sub_arr,main_arr):
  if len(sub_arr) > len(main_arr):
    return False
  for i in range(len(main_arr)):
    if sub_arr == main_arr[i:i+len(sub_arr)]:
      return True
  return False