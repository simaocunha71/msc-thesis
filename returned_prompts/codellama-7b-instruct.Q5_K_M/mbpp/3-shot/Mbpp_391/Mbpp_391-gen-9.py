
def convert_list_dictionary(student_id, student_name, marks):
  dict_list = []
  if len(student_id) == len(student_name) == len(marks):
    for i in range(len(student_id)):
      student_dict = {student_id[i]: {student_name[i]: marks[i]}}
      dict_list.append(student_dict)
    return dict_list


