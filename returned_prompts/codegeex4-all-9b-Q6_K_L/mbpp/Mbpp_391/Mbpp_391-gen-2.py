def convert_list_dictionary(id_list, name_list, score_list):
  result = []
  for i in range(len(id_list)):
    result.append({id_list[i]: {name_list[i]: score_list[i]}})
  return result


