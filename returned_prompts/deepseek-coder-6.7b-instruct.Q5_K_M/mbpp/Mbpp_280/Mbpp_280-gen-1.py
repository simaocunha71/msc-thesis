
def sequential_search(array, item):
  for i in range(len(array)):
    if array[i] == item:
      return (True, i)
  return (False, -1)


