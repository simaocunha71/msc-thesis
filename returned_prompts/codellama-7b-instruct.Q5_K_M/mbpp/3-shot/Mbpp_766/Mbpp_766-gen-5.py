
def pair_wise(my_list: list):
  pairs = []
  for i in range(len(my_list)-1):
    pairs.append((my_list[i],my_list[i+1]))
  return pairs


