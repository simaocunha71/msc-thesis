
def insert_element(lst: list, elem: any) -> list:
  return [elem] + [i for sub in lst for i in (elem, sub)]


