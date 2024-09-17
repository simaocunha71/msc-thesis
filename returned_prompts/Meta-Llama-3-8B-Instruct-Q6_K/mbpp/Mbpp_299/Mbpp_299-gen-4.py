```
def max_aggregate(tuples_list):
    dict_aggregate = {}
    for student, score in tuples_list:
        if student in dict_aggregate:
            dict_aggregate[student] += score
        else:
            dict_aggregate[student] = score
    return max(dict_aggregate.items(), key=lambda x: x[1])
```
The function `max_aggregate` takes a list of tuples as an argument. Each tuple contains a student's name and a score. The function calculates the maximum aggregate by creating a dictionary where the keys are the student's names and the values are the sum of their scores. Then, it returns the student with the maximum aggregate. In case of a tie, it returns the first student with the maximum aggregate.

The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` ensures that the function works correctly by comparing the output with the expected result. The expected result is `('Juan Whelan', 212)`, which is the student with the maximum aggregate. 