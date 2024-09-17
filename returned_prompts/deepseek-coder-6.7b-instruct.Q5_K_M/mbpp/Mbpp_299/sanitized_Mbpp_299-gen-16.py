from collections import defaultdict
def max_aggregate(tuples: list) -> tuple:
  d = defaultdict(int)
  for name, num in tuples:
    d[name] += num
  max_key = max(d, key=d.get)
  return (max_key, d[max_key])