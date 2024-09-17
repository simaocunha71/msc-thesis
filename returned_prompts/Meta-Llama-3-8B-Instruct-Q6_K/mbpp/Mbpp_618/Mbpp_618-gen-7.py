```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists are of different lengths"
    result = []
    for i in range(len(list1)):
        if list2[i] == 0:
            return "Division by zero is not allowed"
        result.append(list1[i] / list2[i])
    return result
```


This function takes two lists as input, and returns a new list where each element is the result of dividing the corresponding elements in the input lists. It also checks if the lists are of the same length and if the second list contains any zeros, and returns an error message in these cases. The division operation is performed using the Python operator `/`, which performs floating-point division. If you want to perform integer division, you can use the `//` operator instead. 

For example, `div_list([4,5,6],[1, 2, 3])` would return `[4.0, 2.5, 2.0]`. 

The unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` ensures that the function works correctly. 

The function also handles the case where the second list contains a zero, and returns an error message in this case. This is because division by zero is not a valid mathematical operation and would cause a runtime error if attempted. 

The function also checks if the lists are of the same length, and returns an error message if they are not. This is because element-wise division only makes sense if the lists are of the same length. 

Overall, this function provides a robust and safe way to perform element-wise division on two lists in Python. 