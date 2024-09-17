def insert_element(lst: list, elem: str) -> list:
  return [elem] + [elem] * len(lst) + lst


