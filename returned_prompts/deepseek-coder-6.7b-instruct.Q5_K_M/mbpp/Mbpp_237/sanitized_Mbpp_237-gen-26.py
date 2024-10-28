from collections import Counter
def check_occurences(lst: list) -> dict:
  lst.reverse()
  return dict(Counter(lst))