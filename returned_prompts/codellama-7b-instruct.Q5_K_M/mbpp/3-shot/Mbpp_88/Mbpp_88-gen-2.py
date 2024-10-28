
def freq_count(my_list):
  freq_dict = {}
  for elem in my_list:
    if elem in freq_dict:
      freq_dict[elem] += 1
    else:
      freq_dict[elem] = 1
  return freq_dict


