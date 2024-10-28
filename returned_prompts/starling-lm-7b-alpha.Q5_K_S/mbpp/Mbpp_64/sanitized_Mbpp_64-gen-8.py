def subject_marks(marks):
    marks.sort(key = lambda x:x[1])
    return marks
marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]