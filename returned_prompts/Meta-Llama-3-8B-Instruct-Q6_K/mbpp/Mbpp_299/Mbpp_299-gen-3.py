```
def max_aggregate(tuples):
    aggregate_dict = {}
    for student, score in tuples:
        if student in aggregate_dict:
            aggregate_dict[student] += score
        else:
            aggregate_dict[student] = score
    return max(aggregate_dict.items(), key=lambda x: x[1])
```
The function max_aggregate takes a list of tuples as input, where each tuple contains a student's name and their score. The function returns the student with the maximum aggregate score.

The function first creates an empty dictionary, aggregate_dict, to store the aggregate scores for each student. Then, it iterates over the input list of tuples. For each tuple, it checks if the student is already in the dictionary. If the student is already in the dictionary, it adds the current score to the student's aggregate score. If the student is not in the dictionary, it adds the student to the dictionary with their current score.

Finally, the function returns the student with the maximum aggregate score using the built-in max function with a lambda function as the key. The lambda function returns the aggregate score for each student, so the max function returns the student with the maximum aggregate score.

The unit test provided ensures that the function works correctly. The test case is:
```
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
```
This test case checks that the function returns the student with the maximum aggregate score, which is 'Juan Whelan' with an aggregate score of 212.