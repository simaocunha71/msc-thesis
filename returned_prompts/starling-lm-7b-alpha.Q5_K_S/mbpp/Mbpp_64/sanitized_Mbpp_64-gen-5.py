def subject_marks(tuples):
    '''
    >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    True
    '''
    return sorted(tuples, key=lambda x:x[1])