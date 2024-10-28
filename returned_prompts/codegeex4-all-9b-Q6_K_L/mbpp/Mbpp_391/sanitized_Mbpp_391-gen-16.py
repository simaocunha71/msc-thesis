def convert_list_dictionary(s_num: list, names: list, scores: list) -> list:
  return [{s_num[i]: {names[i]: scores[i]}} for i in range(len(s_num))]