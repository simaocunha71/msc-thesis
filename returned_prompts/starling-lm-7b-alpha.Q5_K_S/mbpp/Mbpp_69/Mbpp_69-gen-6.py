
def is_sublist(lst, sublst):
  return any(sublst == lst[i:i+len(sublst)] for i in range(len(lst)-len(sublst)+1))


