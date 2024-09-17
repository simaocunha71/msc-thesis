def check_element(nums: list, element: str) -> bool:
  if all(i == element for i in nums):
    return True
  return False