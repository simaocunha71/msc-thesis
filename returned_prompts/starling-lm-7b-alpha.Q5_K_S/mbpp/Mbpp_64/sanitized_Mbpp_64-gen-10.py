def subject_marks(l):
    """
    Sort a list of tuples by the second value of each tuple.

    >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
    [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    """
    return sorted(l, key=lambda x: x[1])