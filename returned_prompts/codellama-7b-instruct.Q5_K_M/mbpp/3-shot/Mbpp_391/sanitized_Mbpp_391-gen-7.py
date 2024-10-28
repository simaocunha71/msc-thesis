def convert_list_dictionary(student_id,name,marks):
  assert len(student_id) == len(name) == len(marks)
  return [
    {s_id: {n: m} for s_id, n, m in zip(student_id, name, marks)}
  ]