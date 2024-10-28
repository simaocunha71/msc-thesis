```
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])
```


The function `subject_marks` takes a list of tuples `subjects` as input, where each tuple contains a subject name and a mark. The function sorts the list of tuples based on the marks in ascending order.

The `sorted` function is used to sort the list, and the `key` argument is set to a lambda function that returns the second element of each tuple (i.e., the mark). This tells the `sorted` function to sort the list based on the marks.

The unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` confirms that the function works correctly. It checks that the function returns a list of tuples sorted by the marks in ascending order.