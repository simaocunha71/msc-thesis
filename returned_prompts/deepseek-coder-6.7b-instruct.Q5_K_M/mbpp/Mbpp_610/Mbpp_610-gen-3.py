
def remove_kth_element(lst: list, k: int) -> list:
  if k <= len(lst):
    del lst[k-1]
  return lst


