def convert_list_dictionary(students,subjects,scores):
  result = []
  for i in range(len(students)):
    result.append({students[i]: {subjects[i]: scores[i]}})
  return result