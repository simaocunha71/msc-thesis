
def max_aggregate(lst):
  dic = {}
  for name, score in lst:
    dic[name] = dic.get(name, 0) + score
  return max(dic.items(), key = lambda x: x[1])


