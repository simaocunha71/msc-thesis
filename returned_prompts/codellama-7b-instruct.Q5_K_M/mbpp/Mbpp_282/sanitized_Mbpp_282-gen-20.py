def sub_list(list_a: list, list_b: list) -> list:
  result = [a-b for a,b in zip(list_a, list_b)]
  return result