```
def max_difference(tuple_list):
    differences = [max(t) - min(t) for t in tuple_list]
    return max(differences)
```


The function takes a list of tuples as input. Each tuple represents a pair of numbers. The function calculates the difference between the maximum and minimum values in each tuple, and then returns the maximum of these differences. This is done using a list comprehension to calculate the differences and the built-in `max` function to find the maximum difference. The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` helps to clarify the expected output of the function. 





The unit test `assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7` helps to clarify the expected output of the function. For the given input `[(3, 5), (1, 7), (10, 3), (1, 2)]`, the function should return `7`, which is the maximum difference between any pair of numbers in the input tuples.