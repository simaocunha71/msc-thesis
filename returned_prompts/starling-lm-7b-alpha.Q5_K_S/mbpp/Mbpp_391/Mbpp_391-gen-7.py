
def convert_list_dictionary(id_list:list,name_list:list,grade_list:list) -> list:
  return [dict(zip(id_list[i],dict(zip(name_list[i],grade_list[i])))) for i in range(len(id_list))]


