
def pair_wise(my_list):
  pairs = [(my_list[i], my_list[i+1]) for i in range(len(my_list)-1)]
  return pairs


