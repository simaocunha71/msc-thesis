def subject_marks(subject_marks_list):
    return sorted(subject_marks_list, key=lambda x: x[1])  # sort by the second element of each tuple