def sort_sublists(list_of_lists):
  return [sorted(sublist) for sublist in list_of_lists]  # or sorted(sublist, key=lambda x: x.lower()) if you want case-insensitive sorting