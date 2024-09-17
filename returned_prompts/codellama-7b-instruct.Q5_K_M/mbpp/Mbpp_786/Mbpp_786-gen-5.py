
def right_insertion(arr,value):
  right_index = 0
  for i in range(len(arr)):
    if arr[i] < value:
      right_index = i + 1
  return right_index


