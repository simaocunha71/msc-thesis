
def sequential_search(array, element):
  index = -1
  for i in range(len(array)):
    if array[i] == element:
      index = i
      break
  return (index != -1, index)


