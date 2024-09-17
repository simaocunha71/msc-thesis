def sample_nam(names:list)->int:
  names_list = []
  for name in names:
    if name[0] != "L":
      names_list.append(name)
  return sum([len(name) for name in names_list])