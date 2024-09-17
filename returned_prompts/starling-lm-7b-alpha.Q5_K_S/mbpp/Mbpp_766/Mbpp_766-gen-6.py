
def pair_wise(lst):
  pair = []
  for i in range(len(lst)-1):
    pair.append((lst[i], lst[i+1]))
  return pair


