def subject_marks(subjects: list) -> list:
  subjects.sort(key = lambda x: x[1])
  return subjects