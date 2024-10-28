def sum(a,b):
  return sum(set(range(min(a,b),max(a,b)+1)) & set(range(min(a,b),max(a,b)+1)))