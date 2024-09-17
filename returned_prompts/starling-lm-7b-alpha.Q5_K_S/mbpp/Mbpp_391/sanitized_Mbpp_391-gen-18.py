def convert_list_dictionary(name_list, student_list, marks_list):
  res = {}
  for i in range(len(name_list)):
    res[name_list[i]] = {}
    res[name_list[i]][student_list[i]] = marks_list[i]
  return res