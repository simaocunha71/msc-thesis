
def get_Inv_Count(arr):
  n = len(arr)
  inv_count = 0

  def merge(arr, l, m, r):
    nonlocal inv_count
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    left_count = 0
    right_count = 0
    temp = []
    while len(left) > 0 and len(right) > 0:
      if left[0] <= right[0]:
        temp.append(left.pop(0))
        left_count += len(right) - m - 1
      else:
        temp.append(right.pop(0))
        right_count += len(left) - l - 1
        inv_count += left_count + right_count
    if left:
      temp.extend(left)
    if right:
      temp.extend(right)
    arr[l:r+1] = temp

  def merge_sort(arr, l, r):
    if l < r:
      m = (l + r) // 2
      merge_sort(arr, l, m)
      merge_sort(arr, m+1, r)
      merge(arr, l, m, r)

  merge_sort(arr, 0, n-1)
  return inv_count


