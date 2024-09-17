
def freq_count(my_list: list)-> dict:
  return {x: my_list.count(x) for x in set(my_list)}


