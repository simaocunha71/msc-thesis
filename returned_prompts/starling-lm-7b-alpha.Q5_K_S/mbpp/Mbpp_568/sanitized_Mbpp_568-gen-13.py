def empty_list(n: int) -> list:
  empty_dict = {}
  empty_list = [empty_dict for _ in range(n)]
  return empty_list