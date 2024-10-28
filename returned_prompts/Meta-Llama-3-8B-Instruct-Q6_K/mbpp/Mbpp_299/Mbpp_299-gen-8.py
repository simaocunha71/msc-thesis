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


The function `max_aggregate` takes a list of tuples as input where each tuple contains a student's name and a score. It calculates the maximum aggregate score by iterating over the input list, summing the scores for each student, and storing the student's name and the total score in a dictionary. Finally, it returns the student with the maximum total score.

The unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` ensures that the function works correctly by comparing the output with the expected result. The expected result is a tuple containing the student's name and the maximum aggregate score, which is 'Juan Whelan' with a total score of 212.