def subject_marks(marks: list) -> list:
    marks.sort(key = lambda x: x[1])
    return marks