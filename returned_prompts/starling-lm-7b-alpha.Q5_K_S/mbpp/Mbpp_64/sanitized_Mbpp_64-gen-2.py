def subject_marks(marks):
    """
    >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
    [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    """
    return sorted(marks, key = lambda x: x[1])