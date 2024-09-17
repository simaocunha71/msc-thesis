```
def is_Monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            increasing = False
        if arr[i-1] < arr[i]:
            decreasing = False
    return increasing or decreasing
```    
    The function `is_Monotonic` checks if the given array is monotonic or not. It takes an array as an input and returns True if the array is monotonic and False otherwise. An array is considered monotonic if it is either strictly increasing or strictly decreasing. The function uses two flags `increasing` and `decreasing` to track these conditions. It iterates over the array, comparing each element with its previous one. If it finds an element that is greater than its previous one, it sets `increasing` to False. If it finds an element that is less than its previous one, it sets `decreasing` to False. At the end, it returns `increasing` or `decreasing`, which is True if the array is monotonic and False otherwise. The unit test `assert is_Monotonic([6, 5, 4, 4]) == True` ensures that the function works correctly for an array that is strictly decreasing.    
    Time complexity: O(n), where n is the length of the array. This is because the function iterates over the array once.    
    Space complexity: O(1), which means the space required does not change with the size of the input array, so it's constant.    
```    
    Note: The function does not consider an array with all equal elements as monotonic. If you want to consider such arrays as monotonic, you can modify the function to return True if the array is either strictly increasing or strictly decreasing, or if all elements are equal.    
    Also, the function does not consider an array with all elements as monotonic. If you want to consider such arrays as monotonic, you can modify the function to return True if the array is either strictly increasing or strictly decreasing, or if all elements are equal.    
    You can also use the following one-liner to solve the problem:    
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1)) or all(arr[i] >= arr[i+1] for i in range(len(arr)-1))    
    This one-liner uses the built-in `all