```
def reverse_Array_Upto_K(arr,k):
    return arr[:k][::-1] + arr[k:]
```


This function takes an array and a position k as input. It returns a new array where the elements from the start to the position k are reversed and the rest of the elements remain the same. The unit test provided in the question ensures the correctness of the function. 

For example, if the input array is [1, 2, 3, 4, 5, 6] and k is 4, the function will return [4, 3, 2, 1, 5, 6]. This is because the elements from the start to the position 4 (inclusive) are reversed (i.e., [1, 2, 3, 4] becomes [4, 3, 2, 1]) and the rest of the elements (i.e., [5, 6]) remain the same. 

The function uses Python's list slicing feature to achieve this. The expression arr[:k][::-1] returns a reversed copy of the sublist from the start to the position k, and the expression arr[k:] returns a copy of the rest of the list. The function then concatenates these two lists to get the desired result. 

The unit test provided in the question checks if the output of the function is as expected. If the output is not as expected, the test will fail, indicating that the function is not working correctly. 

This function assumes that the input array is a list of integers and the position k is a non-negative integer less than or equal to the length of the array. If the input array is not a list of integers or if the position k is invalid, the function may not work correctly or may raise an error. 

In a real-world scenario, you would want to add error checking code to handle these cases. For example, you could check if the input array is a list of integers and if the position k is a valid integer. If not, you could raise an exception or return an error message. 

Here is the modified function that includes error checking:
```
def reverse_Array_Upto_K(arr,k):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("Input list must contain only integers")
    if not isinstance(k, int):
        raise ValueError("Position k must be