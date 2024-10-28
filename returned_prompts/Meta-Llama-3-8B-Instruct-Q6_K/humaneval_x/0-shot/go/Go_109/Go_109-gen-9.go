Here is a solution in Go:

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

Explanation:
The problem is to check if it is possible to get a non-decreasing array by performing right shift operations. 

The function MoveOneBall first checks if the array is empty. If it is, it returns true because an empty array is already sorted.

Then, it sorts the array. If any element in the sorted array is greater than the next element, it means that it is not possible to get a non-decreasing array by performing right shift operations, so the function returns false.

If the function doesn't return false after checking all elements, it means that the array can be sorted by performing right shift operations, so the function returns true.

The time complexity of this solution is O(n log n) because of the sorting, where n is the length of the array. The space complexity is O(n) for the sorted array. 