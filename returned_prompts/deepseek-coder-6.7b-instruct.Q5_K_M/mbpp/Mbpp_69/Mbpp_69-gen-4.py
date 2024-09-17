
def is_sublist(g, s):
  return s in (g[i:i+len(s)] for i in range(len(g)))


