def subject_marks(tuples):
    return sorted(tuples, key=lambda x: x[1])

# test the function
print(subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]))
# Output: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]



The function `subject_marks` takes a list of tuples as an argument. The `sorted` function is used to sort the list. The `key` argument of the `sorted` function is a function that takes a tuple and returns the value that should be used for sorting. In this case, the `key` function is a lambda function that returns the second value of each tuple. The `sorted` function then sorts the list based on the second value of each tuple. The sorted list is then returned by the `subject_marks` function.