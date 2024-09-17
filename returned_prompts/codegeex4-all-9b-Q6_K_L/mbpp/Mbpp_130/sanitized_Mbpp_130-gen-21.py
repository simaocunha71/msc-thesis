from collections import Counter
def max_occurrences(nums: list) -> int:
  counter = Counter(nums)
  max_freq = max(list(counter.values()))
  for item, freq in counter.items():
    if freq == max_freq:
      return item