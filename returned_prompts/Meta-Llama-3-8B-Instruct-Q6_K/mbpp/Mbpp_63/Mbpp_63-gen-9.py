```
def max_difference(tuples):
    return max(end - start for start, end in tuples) - min(start for start, _ in tuples)
```

The function `max_difference` takes a list of tuples as input, where each tuple contains a start and an end value. It calculates the maximum difference between any two points in the list by subtracting the minimum start value from the maximum end value.

The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` helps to understand the problem better. It shows that the function should return the maximum difference between any two points in the list. 

The time complexity of this function is O(n), where n is the number of tuples in the input list. This is because it iterates over the list twice: once to find the minimum start value and once to find the maximum end value. The space complexity is O(1), as it only uses a constant amount of space to store the minimum start value and the maximum end value. 