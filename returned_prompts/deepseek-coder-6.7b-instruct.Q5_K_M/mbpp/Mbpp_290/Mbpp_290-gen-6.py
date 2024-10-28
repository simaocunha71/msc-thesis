
def max_length(list_of_lists):
  return max(enumerate(list_of_lists), key=lambda x: len(x[1]))


