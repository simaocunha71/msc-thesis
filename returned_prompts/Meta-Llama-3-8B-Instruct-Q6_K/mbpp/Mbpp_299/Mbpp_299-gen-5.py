```
def max_aggregate(lst):
    aggregate = {}
    for student, score in lst:
        if student in aggregate:
            aggregate[student] += score
        else:
            aggregate[student] = score
    return max(aggregate.items(), key=lambda x: x[1])
```
The problem asks to write a function that calculates the maximum aggregate from a list of tuples. Each tuple contains the name of a student and their score. The function should return the student with the maximum aggregate score.

The given unit test `assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)` helps to understand the problem better. It shows that the function should return the student with the maximum total score.

Here is the solution:
The function `max_aggregate` initializes an empty dictionary `aggregate`. It then iterates over the list of tuples. For each tuple, it checks if the student is already in the `aggregate` dictionary. If the student is already in the dictionary, it adds the score to their existing total. If the student is not in the dictionary, it adds the student to the dictionary with their score as the total. Finally, it returns the student with the maximum total score using the `max` function with a lambda function as the key to sort the items in the dictionary.

This solution has a time complexity of O(n), where n is the number of tuples in the list, because it iterates over the list once. The space complexity is also O(n), because in the worst case, it needs to store all students in the `aggregate` dictionary.