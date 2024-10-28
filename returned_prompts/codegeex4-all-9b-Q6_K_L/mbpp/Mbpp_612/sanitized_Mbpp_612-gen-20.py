def merge(lists):
  merged = [list(i) for i in zip(*lists)]
  return merged