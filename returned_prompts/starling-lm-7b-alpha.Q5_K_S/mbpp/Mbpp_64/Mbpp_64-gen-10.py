def subject_marks(l):
    """
    Sort a list of tuples by the second value of each tuple.

    >>> subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])
    [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
    """
    return sorted(l, key=lambda x: x[1])

# Created by: Ekadot
# Date: 23/07/2020

"""
Explanation:
The given function uses the sorted() function to sort a list of tuples by the second value of each tuple. It takes a list of tuples as input and uses a lambda function as the key argument to specify that the second value of each tuple should be used for sorting. The lambda function takes a tuple as input and returns the second value of the tuple (i.e., x[1]). The sorted() function then sorts the list of tuples based on the second value of each tuple, and returns the sorted list of tuples as the output.
"""

# Tests:
print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))  # [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
print(subject_marks([('Maths', 97), ('Science', 90), ('English', 88), ('Social sciences', 82)]))  # [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
print(subject_marks([('Maths', 97), ('Maths', 97), ('Science', 90), ('Science', 90)]))  # [('Maths', 97), ('Maths', 97), ('Science', 90), ('Science', 90)]
print