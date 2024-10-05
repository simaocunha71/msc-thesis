The problem can be solved by simply performing the right shift operation until the array is sorted. Here is the solution:

```go
import (
    "math"
    "sort"
)

func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    for {
        done := true
        for i := 0; i < len(arr)-1; i++ {
            if arr[i] > arr[i+1] {
                done = false
                break
            }
        }
        if done {
            return true
        }
        if !done {
            // Perform right shift operation
            last := arr[len(arr)-1]
            arr = append([]int{}, arr[1:]...)
            arr = append(arr, last)
        }
    }
}
```

In this solution, we iterate through the array and check if it's already sorted. If it's sorted, we return true. If not, we perform a right shift operation by moving the last element to the beginning of the array and continue the iteration until the array is sorted. If the array is empty, we return true. The time complexity is O(n^2) and the space complexity is O(n), where n is the length of the array.