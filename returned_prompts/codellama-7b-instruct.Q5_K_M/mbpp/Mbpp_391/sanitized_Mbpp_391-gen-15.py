def convert_list_dictionary(stud_id: list, stud_name: list, marks: list) -> list:
  dict_list = []
  for i in range(len(stud_id)):
    dict_list.append({stud_id[i]: {stud_name[i]: marks[i]}})
  return dict_list