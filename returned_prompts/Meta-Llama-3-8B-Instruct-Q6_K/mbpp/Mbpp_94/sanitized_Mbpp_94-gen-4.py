def index_minimum(lst):
  return min(lst, key=lambda x: x[1])[0]  # returns the first value of the tuple with the smallest second value. 