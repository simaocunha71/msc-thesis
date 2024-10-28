
def unique_sublists(nums: list) -> dict:
  return {tuple(i) for i in nums}.fromkeys(nums).keys()


