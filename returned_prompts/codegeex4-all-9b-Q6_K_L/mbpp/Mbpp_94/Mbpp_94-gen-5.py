def index_minimum(tuples):
  index = tuples.index(min(tuples, key=lambda x: x[1]))
  return tuples[index][0]

