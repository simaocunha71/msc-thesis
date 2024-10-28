def insert_element(test_list: list, test_elem: str) -> list:
  new_list = [test_elem] * len(test_list)
  new_list = new_list + test_list
  return new_list