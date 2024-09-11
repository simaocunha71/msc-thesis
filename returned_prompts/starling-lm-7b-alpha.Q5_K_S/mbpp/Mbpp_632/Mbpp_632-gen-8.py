def move_zero(list):
    zeros = []
    for i in range(len(list)):
        if list[i] != 0:
            print(list[i])
        else:
            zeros.append(list[i])
    return zeros + list


```
move_zero([1,0,2,0,3,4])
```

Explanation:
To solve this problem we can create a function that will go through the list and for every non-zero element print it and add to the new list. After that we return the new list concatenated with the zeros list.

Here's the step-by-step explanation of the code:

1. We create an empty list called `zeros` that will contain all the zeros.
2. We iterate over the input list using a for loop.
3. Inside the loop we check if the current element is zero or not.
4. If the current element is not zero, we print it and add to the `zeros` list.
5. After the loop is finished, we return the concatenation of the `zeros` list with the non-zero elements.

This will ensure that all the zeroes are moved to the end of the list.

Note: The print statement inside the loop is just to demonstrate that the non-zero elements are being printed. In a real implementation, you would probably remove it or replace it with another logic depending on your use case.

The time complexity of this solution is O(n), where n is the length of the input list. This is because we are iterating over the list once. The space complexity is also O(n), as we are creating a new list to store the non-zero elements.

Here's the code again, but without the print statement:

```python
def move_zero(list):
    zeros = []
    for i in range(len(list)):
        if list[i] != 0:
            zeros.append(list[i])
    return zeros + list
```

You can test this function with the given assert statement:

```python
assert move_zero([1,0,2,0,3,4]) == [1,2,3,