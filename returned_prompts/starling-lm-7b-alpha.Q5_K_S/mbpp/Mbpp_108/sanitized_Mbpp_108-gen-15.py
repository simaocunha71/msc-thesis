def merge_sorted_list(nums_1: list,nums_2: list,nums_3: list) -> list:
  sorted_nums = nums_1 + nums_2 + nums_3
  sorted_nums.sort()
  return sorted_nums