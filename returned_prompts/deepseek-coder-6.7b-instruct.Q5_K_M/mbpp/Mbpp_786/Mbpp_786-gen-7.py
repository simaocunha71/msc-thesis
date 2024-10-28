
import bisect
def right_insertion(nums: list, num: int) -> int:
  return bisect.bisect_right(nums, num)


