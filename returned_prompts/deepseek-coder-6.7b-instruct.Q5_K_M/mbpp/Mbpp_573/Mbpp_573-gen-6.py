
from collections import Counter
def unique_product(lst: list) -> int:
  c = Counter(lst)
  unique_values = [k for k, v in c.items() if v == 1]
  product = 1
  for num in unique_values:
    product *= num
  return product


