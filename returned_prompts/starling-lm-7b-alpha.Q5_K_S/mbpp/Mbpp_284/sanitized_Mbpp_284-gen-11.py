def check_element(nums: list, element: str) -> bool:
  return all(i==element for i in nums)