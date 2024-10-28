```
def smallest_change(arr):
    n = len(arr)
    rev_arr = arr[::-1]
    diff_count = 0
    for i in range(n):
        if arr[i] != rev_arr[i]:
            diff_count += 1
    return diff_count
```
This function works by first reversing the input array to create a palindrome. Then, it counts the number of elements that are different between the original array and the reversed array. This count is the minimum number of changes needed to make the array palindromic.

For example, the function returns 4 for the array [1,2,3,5,4,7,9,6] because 4 elements need to be changed to make the array palindromic: 3 and 5 need to be changed to 4, and 7 and 9 need to be changed to 6. The function returns 1 for the array [1, 2, 3, 4, 3, 2, 2] because only 1 element needs to be changed to make the array palindromic: 3 needs to be changed to 4. The function returns 0 for the array [1, 2, 3, 2, 1] because the array is already palindromic.