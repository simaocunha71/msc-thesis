The problem is asking to split a list at the nth element and add the first part to the end. For example, if the input list is [12,10,5,6,52,36] and n is 2, the output should be [5,6,52,36,12,10].

Here is the Python function that solves this problem:
```
def split_Arr(A, n):
    return A[n:] + A[:n]
```
This function uses list slicing to split the list at the nth element. The expression `A[n:]` gets all elements from the nth element to the end of the list, and the expression `A[:n]` gets all elements from the beginning of the list to the nth element. The `+` operator is used to concatenate these two lists in reverse order.

The unit test `assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]` ensures that the function works correctly. It checks if the output of the function with the input list [12,10,5,6,52,36] and n = 2 is equal to the expected output [5,6,52,36,12,10]. If the function is implemented correctly, this test should pass.