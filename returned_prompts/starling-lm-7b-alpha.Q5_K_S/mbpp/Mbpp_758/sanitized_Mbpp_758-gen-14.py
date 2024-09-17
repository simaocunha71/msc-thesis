def unique_sublists(lists):
  return {tuple(sublist) for sublist in lists}.fromkeys(lists).map(lambda x: lists.count(x))