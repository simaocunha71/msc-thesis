```
def remove_elements(lst1, lst2):
    return [i for i in lst1 if i not in lst2]
```


The unit test provided helps in understanding the problem better. It states that the function should remove all elements present in `lst2` from `lst1`. The unit test is `assert remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 10]`.

The solution uses list comprehension to achieve this. It iterates over each element `i` in `lst1` and checks if it is not present in `lst2`. If it is not present, it includes it in the resulting list. The resulting list is then returned.

The unit test provided helps in verifying the correctness of the solution. The test checks if the function returns the expected output for the given input. If the output matches the expected output, it means the function is working correctly. If the output does not match the expected output, it means the function is not working correctly and needs to be modified. In this case, the function is working correctly and returns the expected output. Therefore, the unit test passes.