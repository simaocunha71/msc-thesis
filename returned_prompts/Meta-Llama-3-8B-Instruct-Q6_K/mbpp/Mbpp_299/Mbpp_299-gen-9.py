```
def max_aggregate(tuples):
    aggregate = {}
    for student, score in tuples:
        if student in aggregate:
            aggregate[student] += score
        else:
            aggregate[student] = score
    return max(aggregate.items(), key=lambda x: x[1])
```
The function `max_aggregate` takes a list of tuples as input where each tuple contains a student's name and their score. It calculates the maximum aggregate score by summing up the scores for each student. If a student appears multiple times in the input list, their total score will be the sum of their scores. The function returns the student with the maximum aggregate score and their aggregate score.

The unit test provided ensures that the function works correctly by checking that the student 'Juan Whelan' with an aggregate score of 212 is returned as the maximum aggregate. 

The time complexity of this function is O(n) where n is the number of tuples in the input list, as it iterates over the list once to calculate the aggregate scores. The space complexity is also O(n), as in the worst case, all students may have the same name and their scores will be stored in the dictionary. 