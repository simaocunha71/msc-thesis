
def right_insertion(arr, val):
  # find the right most index of the value less than val
  right_index = len(arr) - 1
  while right_index >= 0 and arr[right_index] > val:
    right_index -= 1

  # find the left most index of the value greater than val
  left_index = -1
  while left_index + 1 < right_index and arr[left_index + 1] < val:
    left_index += 1

  return left_index + 1


