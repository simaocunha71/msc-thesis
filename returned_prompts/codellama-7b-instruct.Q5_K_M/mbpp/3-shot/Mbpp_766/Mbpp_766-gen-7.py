
def pair_wise(my_list):
  result = []
  for i in range(len(my_list)-1):
    for j in range(i+1, len(my_list)):
      result.append((my_list[i], my_list[j]))
  return result


