```
def sum_negativenum(lst):
    return sum(num for num in lst if num < 0)
```


The function `sum_negativenum` takes a list of numbers as input. It uses a generator expression to iterate over the list and sum up all the numbers that are less than 0. The `sum` function is then used to calculate the sum of these negative numbers. The unit test `assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32` ensures that the function works correctly. 

This solution has a time complexity of O(n), where n is the number of elements in the input list, because it needs to iterate over the entire list once. The space complexity is O(1), because it uses a constant amount of space to store the sum and the generator expression. 

This solution is more efficient than a naive solution that would involve iterating over the list twice, once to find the negative numbers and once to sum them up. The `sum` function is able to handle the generator expression in a single pass, making this solution more efficient and more Pythonic. 