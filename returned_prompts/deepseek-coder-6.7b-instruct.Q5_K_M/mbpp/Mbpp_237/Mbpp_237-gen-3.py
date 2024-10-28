
def check_occurences(lst):
  return {tuple(sorted(i)): lst.count(i) for i in lst}


