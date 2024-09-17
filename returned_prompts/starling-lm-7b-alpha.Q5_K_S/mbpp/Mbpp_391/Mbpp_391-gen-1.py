
def convert_list_dictionary(id_list: list, name_list: list, score_list: list) -> list:
  result = []
  for i, j, k in zip(id_list, name_list, score_list):
    result.append({i: {j: k}})
  return result


