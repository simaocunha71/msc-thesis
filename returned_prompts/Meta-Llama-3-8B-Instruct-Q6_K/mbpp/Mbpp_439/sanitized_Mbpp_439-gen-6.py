def multiple_to_single(nums):
  return int("".join(map(str, nums)))  # convert each number to string, join them, and convert back to integer.  # NOQA: F841