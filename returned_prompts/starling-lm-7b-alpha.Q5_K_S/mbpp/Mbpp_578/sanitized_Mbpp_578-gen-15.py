def interleave_lists(nums_1: list,nums_2: list,nums_3: list) -> list:
  return [nums_1[i%len(nums_1)] + nums_2[i%len(nums_2)] + nums_3[i%len(nums_3)] for i in range(len(nums_1))]