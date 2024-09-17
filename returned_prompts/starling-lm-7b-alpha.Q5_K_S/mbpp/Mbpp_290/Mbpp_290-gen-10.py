
def max_length(lists):
  length = max(map(len, lists))
  return (length, [i for i in lists if len(i) == length])


