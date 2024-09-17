
def convert_list_dictionary(students_id, students_name, scores):
  students_dictionary = []
  for i in range(len(students_id)):
    students_dictionary.append({students_id[i]:{students_name[i]: scores[i]}})
  return students_dictionary


