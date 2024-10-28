You can solve this problem by using Python's built-in sorting function and a lambda function to specify the sorting key. The lambda function returns the second element of each tuple, which is used to sort the list.

Here is the solution:
```
def subject_marks(tuples):
    return sorted(tuples, key=lambda x: x[1])
```
This function takes a list of tuples as input, sorts the list based on the second element of each tuple, and returns the sorted list.

The unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` ensures that the function works correctly. It checks that the function returns the expected sorted list.

Note: The lambda function `lambda x: x[1]` returns the second element of each tuple, which is used to sort the list. The `sorted` function is then used to sort the list based on this key. The resulting sorted list is returned by the function.