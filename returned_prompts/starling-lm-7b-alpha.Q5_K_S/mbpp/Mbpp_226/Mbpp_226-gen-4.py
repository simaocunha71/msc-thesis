
def odd_values_string(string:str):
  odd_index_list = []
  for i in range(len(string)):
    if i % 2 != 0:
      odd_index_list.append(string[i])
  return ''.join(odd_index_list)


