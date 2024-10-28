
def convert_list_dictionary(student_id, names, scores):
  return [
    {student_id[i]: {names[i]: scores[i]}}
    for i in range(len(student_id))
  ]


