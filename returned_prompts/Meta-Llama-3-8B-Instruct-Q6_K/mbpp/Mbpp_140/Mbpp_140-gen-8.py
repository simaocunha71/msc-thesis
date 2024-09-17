```
def extract_singly(lst):
    return set(num for sublist in lst for num in sublist)
```



In this problem, we are asked to write a function that takes a list of lists as input and returns a set of numbers. Each sublist in the input list contains a sequence of numbers.

The problem is not clearly defined because it does not specify how the sublists are related to the original list. However, based on the provided unit test, it seems that we need to flatten the list of lists into a single set of numbers.

The unit test `assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])` suggests that the function should return a set containing all the numbers from the sublists, without duplicates.

Here is a Python solution for this problem:
```
def extract_singly(lst):
    return set(num for sublist in lst for num in sublist)
```
This function uses a generator expression to iterate over each sublist in the input list, and then over each number in each sublist. The `set` function is used to remove duplicates from the resulting list of numbers. The function returns the resulting set of numbers.