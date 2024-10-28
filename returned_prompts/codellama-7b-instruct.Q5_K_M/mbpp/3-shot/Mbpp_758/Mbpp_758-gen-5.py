
def unique_sublists(my_list):
  count = {}
  for sublist in map(tuple, my_list):
    if sublist not in count:
      count[sublist] = 0
    count[sublist] += 1
  return count


