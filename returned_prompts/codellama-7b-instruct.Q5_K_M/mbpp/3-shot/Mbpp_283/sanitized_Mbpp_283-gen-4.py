def validate(n):
  d = {}
  for i in str(n):
    if i in d.keys():
      if d[i] >= int(i):
        return False
      else:
        d[i] += 1
    else:
      d[i] = 1
  return True