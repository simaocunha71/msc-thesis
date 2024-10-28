```
def max_difference(tuples):
    differences = [abs(t[1] - t[0]) for t in tuples]
    return max(differences)
```
The problem is asking you to find the maximum difference between the available pairs in the given tuple list. The tuple list contains pairs of integers, and we need to find the maximum difference between these pairs.

The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` helps us understand that the input is a list of tuples, where each tuple contains two integers. We need to find the maximum difference between these pairs.

Here is the solution:
```
def max_difference(tuples):
    differences = [abs(t[1] - t[0]) for t in tuples]
    return max(differences)
```
This function uses a list comprehension to calculate the differences between the pairs in the tuple list. It then returns the maximum difference. The `abs` function is used to ensure that the differences are always positive. The `max` function is used to find the maximum difference.

For example, if we call `max_difference([(3, 5), (1, 7), (10, 3), (1, 2)])`, the function will return `7`, which is the maximum difference between the pairs in the tuple list. The pairs are `(3, 5)`, `(1, 7)`, `(10, 3)`, and `(1, 2)`, and the differences are `2`, `6`, `7`, and `1`, respectively. The maximum difference is `7`.