def extract_singly(lst_of_lst: list) -> list:
  flat_lst = [num for sublist in lst_of_lst for num in sublist]
  return flat_lst