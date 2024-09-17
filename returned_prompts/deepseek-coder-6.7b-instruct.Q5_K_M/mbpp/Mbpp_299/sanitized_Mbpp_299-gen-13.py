def max_aggregate(lst):
  d = {}
  for name, num in lst:
    if name in d:
      d[name] += num
    else:
      d[name] = num
  max_val = max(d.values())
  for key in d:
    if d[key] == max_val:
      return (key, max_val)