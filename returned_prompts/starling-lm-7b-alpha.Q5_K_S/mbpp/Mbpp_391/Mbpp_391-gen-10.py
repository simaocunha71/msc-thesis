
def convert_list_dictionary(student_ids:list,student_names:list,marks:list) -> list:
  return [dict(zip(student_ids,dict(zip(student_names,marks))))]


