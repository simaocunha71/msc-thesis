def check_element(nums: list, element: str) -> bool:
  return all(x == element for x in nums)