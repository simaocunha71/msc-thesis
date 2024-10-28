
def unique_sublists(l:list)->dict:
  sublists = {}
  for i in l:
    try:
      sublists[tuple(i)].append(i)
    except KeyError:
      sublists[tuple(i)] = [i]
  return sublists


