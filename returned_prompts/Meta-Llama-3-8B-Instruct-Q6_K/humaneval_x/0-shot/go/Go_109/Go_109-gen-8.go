Here is the solution in Go:

```go
import (
    "math"
    "sort"
)

func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    sort.Ints(arr)
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}
```

This function takes an array of integers as input and returns a boolean value. It first checks if the array is empty. If it is, it returns `true` as it is possible to get a non-decreasing array by performing no operations. Then, it sorts the array in non-decreasing order. If the sorted array is the same as the original array, it returns `true`. Otherwise, it returns `false`. This is because it is not possible to get a non-decreasing array by performing right shift operations if the array is not already sorted. The time complexity of this function is O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(1) as it only uses a constant amount of space.