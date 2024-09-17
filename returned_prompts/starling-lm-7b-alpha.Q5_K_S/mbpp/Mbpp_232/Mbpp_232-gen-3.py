
def larg_nnum(nums: list,n: int) -> list:
  sorted_nums = sorted(nums, reverse=True)[:n]
  return sorted_nums


