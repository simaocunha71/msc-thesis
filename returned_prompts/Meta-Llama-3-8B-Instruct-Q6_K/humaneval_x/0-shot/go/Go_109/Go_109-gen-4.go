Here is the solution to the problem:

```go
func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    minVal := math.MinFloat64
    for _, val := range arr {
        if val < minVal {
            minVal = val
        }
    }
    return arr[0] >= minVal
}
```

Explanation:

The solution is quite simple. If the array is empty, return true as there are no elements to be sorted. 

Otherwise, find the minimum value in the array. If the first element of the array is greater than or equal to the minimum value, then it's possible to get the array sorted in non-decreasing order by performing right shift operations. 

This is because the right shift operation can move the smallest element to the front of the array, and the array can be sorted by repeatedly shifting the smallest element to the front until the array is sorted. 

If the first element is less than the minimum value, then it's not possible to get the array sorted in non-decreasing order by performing right shift operations, so return false. 

The time complexity of this solution is O(n), where n is the length of the array, because we need to find the minimum value in the array. The space complexity is O(1), because we only use a constant amount of space to store the minimum value and the result. 