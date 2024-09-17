
def is_majority(arr: list, n: int, num: int) -> bool:
  """
  TC: O(1)
  SC: O(1)
  """
  # Write your code here
  c = 0
  for i in range(n):
    if arr[i] == num:
      c += 1
    if c > n//2:
      return True
  return False


