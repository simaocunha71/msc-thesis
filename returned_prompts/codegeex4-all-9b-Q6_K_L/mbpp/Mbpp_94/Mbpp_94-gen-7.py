def index_minimum(tuples):
  minimum = min(tuples, key=lambda x: x[1])
  return minimum[0]

