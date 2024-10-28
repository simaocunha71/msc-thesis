def sum_even_and_even_index(nums:list)->int:
  even_nums = [num for index, num in enumerate(nums) if index % 2 == 0 and num % 2 == 0]
  return sum(even_nums)