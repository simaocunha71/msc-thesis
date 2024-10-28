```
func CanArrange(arr []int) int {
    n := len(arr)
    if n == 0 {
        return -1
    }
    max := -1
    for i := 1; i < n; i++ {
        if arr[i] <= arr[i-1] {
            max = i
        }
    }
    return max
}
```


Explanation:
This function iterates through the array starting from the second element (index 1). It checks if the current element is less than or equal to the previous element. If it is, it updates the `max` variable with the current index. If no such element is found, `max` remains -1. Finally, the function returns the `max` value.

Time Complexity: O(n)
Space Complexity: O(1)

Example Outputs:
- For the input `[1,2,4,3,5]`, the function returns `3` because the largest index of an element which is not greater than or equal to the element immediately preceding it is `3` (at index 3, the element `3` is not greater than or equal to the element `4` at index 2).
- For the input `[1,2,3]`, the function returns `-1` because no element in the array is less than or equal to the element immediately preceding it.