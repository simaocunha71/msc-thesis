
def pack_consecutive_duplicates(my_list):
  return [[k, *l] for k, l in itertools.groupby(my_list)]


