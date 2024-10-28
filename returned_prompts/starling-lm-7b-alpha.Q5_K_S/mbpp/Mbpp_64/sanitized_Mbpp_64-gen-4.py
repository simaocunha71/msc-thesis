def subject_marks(marks_list):
    # sorting the list of tuples according to the second element of the tuple
    marks_list.sort(key=lambda x: x[1])
    return marks_list