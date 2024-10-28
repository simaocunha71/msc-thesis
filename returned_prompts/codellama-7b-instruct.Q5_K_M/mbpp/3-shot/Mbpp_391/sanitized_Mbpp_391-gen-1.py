def convert_list_dictionary(student_ids, names, scores):
  assert len(student_ids) == len(names) == len(scores)
  return [{student_ids[i]: {names[i]: scores[i]}} for i in range(len(student_ids))]