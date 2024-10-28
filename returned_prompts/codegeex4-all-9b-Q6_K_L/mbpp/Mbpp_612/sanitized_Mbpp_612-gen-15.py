def merge(lists):
  res = [[], []]
  for l in lists:
    res[0].append(l[0])
    res[1].append(l[1])
  return res