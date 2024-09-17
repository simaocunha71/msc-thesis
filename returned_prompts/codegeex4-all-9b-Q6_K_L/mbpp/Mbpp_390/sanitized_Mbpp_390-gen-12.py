def add_string(nums: list, format_str: str) -> list:
  return [format_str.format(num) for num in nums]