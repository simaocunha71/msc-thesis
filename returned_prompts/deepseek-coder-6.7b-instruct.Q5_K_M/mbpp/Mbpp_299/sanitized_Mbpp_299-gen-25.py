def max_aggregate(lst):
  sums = {}
  for name, num in lst:
    if name in sums:
      sums[name] += num
    else:
      sums[name] = num
  max_name = max(sums, key=sums.get)
  return (max_name, sums[max_name])