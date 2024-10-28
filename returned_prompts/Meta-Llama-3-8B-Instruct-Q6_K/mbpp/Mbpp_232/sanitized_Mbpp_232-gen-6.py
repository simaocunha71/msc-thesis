from typing import List
def larg_nnum(lst: List[int], n: int) -> List[int]:
  return sorted(lst, reverse=True)[:n]  # This will return the n largest items from the list