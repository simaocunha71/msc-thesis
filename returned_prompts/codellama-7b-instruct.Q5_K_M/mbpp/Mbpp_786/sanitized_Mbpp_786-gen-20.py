def right_insertion(arr,num):
  right_idx = 0
  for i in range(len(arr)):
    if arr[i] > num:
      right_idx = i
      break
  return right_idx