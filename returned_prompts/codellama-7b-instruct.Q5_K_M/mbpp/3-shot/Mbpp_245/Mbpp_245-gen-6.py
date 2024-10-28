
def max_sum(arr):
  def is_bitonic(arr):
    for i in range(len(arr)-1):
      if arr[i] < arr[i+1]:
        return False
    return True

  def max_sum(arr):
    def helper(arr, start, end):
      if start == end:
        return arr[start]
      mid = (start + end) // 2
      left = helper(arr, start, mid)
      right = helper(arr, mid+1, end)
      if is_bitonic(arr[start:end]):
        return left + right
      else:
        return max(left, right)

    return helper(arr, 0, len(arr)-1)

  if not is_bitonic(arr):
    raise ValueError('Input array is not bitonic')
  return max_sum(arr)


