def freq_count(my_list: list) -> dict:
  return {k: my_list.count(k) for k in set(my_list)}