
def max_aggregate(lst):
  d = {}
  for name, num in lst:
    if name in d:
      d[name] += num
    else:
      d[name] = num
  return max(d.items(), key=lambda x: x[1])


