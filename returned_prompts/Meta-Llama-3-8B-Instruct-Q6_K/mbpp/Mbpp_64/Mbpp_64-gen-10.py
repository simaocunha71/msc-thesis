```
def subject_marks(subjects):
    return sorted(subjects, key=lambda x: x[1])
```


This function sorts a list of tuples based on the second value of each tuple. The `sorted` function is used with a `key` argument set to a lambda function that returns the second value of each tuple. This means that the tuples will be sorted based on the values in the second position.

The provided unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` helps to clarify the expected behavior of the function. It shows that the function should return a sorted list of tuples, with the tuples sorted based on the values in the second position. In this case, the list is sorted in ascending order, with the tuple with the smallest value in the second position first, and the tuple with the largest value in the second position last. 





Note: 
The provided unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` helps to clarify the expected behavior of the function. It shows that the function should return a sorted list of tuples, with the tuples sorted based on the values in the second position. In this case, the list is sorted in ascending order, with the tuple with the smallest value in the second position first, and the tuple with the largest value in the second position last. 
The provided unit test helps to clarify the expected behavior of the function. It shows that the function should return a sorted list of tuples, with the tuples sorted based on the values in the second position. In this case, the list is sorted in ascending order, with the tuple with the smallest value in the second position first, and the tuple with the largest value in the second position last. 
The provided unit test `assert subject_marks([('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)])==[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]` helps to clarify the expected behavior