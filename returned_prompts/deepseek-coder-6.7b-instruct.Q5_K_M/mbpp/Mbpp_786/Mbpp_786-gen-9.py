
import bisect
def right_insertion(nums: list, val: int) -> int:
  return bisect.bisect_right(nums, val)


