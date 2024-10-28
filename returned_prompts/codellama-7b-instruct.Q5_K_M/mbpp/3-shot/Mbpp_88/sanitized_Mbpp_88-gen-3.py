def freq_count(my_list):
  return {i: my_list.count(i) for i in set(my_list)}