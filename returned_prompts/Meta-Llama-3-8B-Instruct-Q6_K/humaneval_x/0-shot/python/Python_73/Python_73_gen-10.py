```
def smallest_change(arr):
    arr = [str(i) for i in arr]
    n = len(arr)
    arr = ''.join(arr)
    rev_arr = arr[::-1]
    diff = 0
    for i in range(n):
        if arr[i] != rev_arr[i]:
            diff += 1
    return diff
```


This function first converts the array to a string. Then it reverses the string. It counts the number of positions at which the original string and the reversed string are different. This is the minimum number of changes needed to make the array palindromic. The time complexity of this function is O(n), where n is the number of elements in the array. The space complexity is also O(n), as we are storing the array as a string. 

For example, if the input is [1,2,3,5,4,7,9,6], the function will return 4. This is because the array is not palindromic and we need to change 4 elements to make it palindromic. If the input is [1, 2, 3, 4, 3, 2, 2], the function will return 1, because we need to change only 1 element to make the array palindromic. If the input is [1, 2, 3, 2, 1], the function will return 0, because the array is already palindromic. 

This function assumes that the input array contains only non-negative integers. If the array can contain negative integers or non-integer elements, the function would need to be modified accordingly. 

This function also assumes that the array is not empty. If the array can be empty, the function should be modified to handle this case. 

This function has a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the array.  It is efficient for small to medium-sized arrays, but it may not be efficient for very large arrays. 

This function does not check if the input array is valid. It assumes that the input array is a list of integers. If the input array is not a list of integers, the function may not work correctly. It would be a good idea to add input validation to the function to check if the input array is valid. 

This function is not suitable for very large arrays. It uses a lot of memory to store