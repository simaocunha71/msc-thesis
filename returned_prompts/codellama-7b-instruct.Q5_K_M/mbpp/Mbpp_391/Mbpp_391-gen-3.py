
def convert_list_dictionary(student_id, student_name, marks):
  student_dict = {}
  for i in range(len(student_id)):
    student_dict[student_id[i]] = {student_name[i]: marks[i]}
  return student_dict


