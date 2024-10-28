def add_string(nums: list,format_string: str) -> list:
  return [format_string.format(i) for i in nums]