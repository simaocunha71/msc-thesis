def merge(lists: list) -> list:
  first_elements = [sublist[0] for sublist in lists]
  second_elements = [sublist[1] for sublist in lists]
  return [first_elements, second_elements]

