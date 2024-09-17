def check_occurences(tup_list: list) -> dict:
  return dict((x,tup_list.count(x)) for x in tup_list)

