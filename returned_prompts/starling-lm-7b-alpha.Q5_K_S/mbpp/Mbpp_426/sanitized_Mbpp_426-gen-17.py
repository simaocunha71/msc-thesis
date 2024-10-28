def filter_oddnumbers(nums:list) -> list:
  return list(filter(lambda x: x % 2 == 1, nums))