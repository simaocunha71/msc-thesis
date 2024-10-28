Here is a solution using sorting and checking if the array is sorted:

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
    for i := 1; i < len(arr); i++ {
        if arr[i-1] > arr[i] {
            return false
        }
    }
    return true
}
```

This function sorts the array and then checks if the array is sorted in non-decreasing order. If the array is sorted, it returns true, otherwise it returns false. If the array is empty, it returns true.

The time complexity of this function is O(n log n) due to the sorting operation, where n is the length of the array. The space complexity is O(1) as it only uses a fixed amount of space to store the temporary results.