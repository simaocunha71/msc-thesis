def check_occurences(tup_list: list) -> dict:
  return {k: tup_list.count(k) for k in set(tup_list)}