def index_minimum(tuples):
  return min(tuples, key=lambda x: x[1])[0]  # Use the min function with a custom key to find the tuple with the smallest second value, then return the first value of that tuple.