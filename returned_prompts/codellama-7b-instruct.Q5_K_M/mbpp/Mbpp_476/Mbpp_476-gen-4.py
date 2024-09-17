
def big_sum(arr):
  largest = 0
  smallest = 0
  for i in range(len(arr)):
    if arr[i] > largest:
      largest = arr[i]
    if arr[i] < smallest:
      smallest = arr[i]
  return largest + smallest


