```
def div_list(list1, list2):
    if len(list1) != len(list2):
        return "Lists are not of the same length"
    return [i/j for i, j in zip(list1, list2)]
```
This function takes two lists as input and returns a new list where each element is the result of dividing the corresponding elements from the input lists. If the lists are not of the same length, the function returns an error message.

The function uses the built-in zip function to iterate over the input lists in parallel, and a list comprehension to create the new list. The division is performed using the / operator, which performs floating-point division in Python.

The unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` ensures that the function returns the correct result for the given input.