
def find_min_diff(arr: list,target_sum: int) -> int:
  arr.sort()
  min_diff = float("inf")
  for i in range(len(arr)-1):
    if arr[i]+arr[i+1] < min_diff:
      min_diff = arr[i]+arr[i+1]
  return min_diff


