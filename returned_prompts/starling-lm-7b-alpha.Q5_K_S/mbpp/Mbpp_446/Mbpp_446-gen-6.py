
def count_Occurrence(tuple_inp, list_inp):
  count = 0
  for i in tuple_inp:
    if i in list_inp:
      count += 1
  return count


