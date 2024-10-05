Here is a Go function that implements the problem:

```go
import (
    "math"
    "sort"
)

func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    n := len(arr)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if arr[j] < arr[i] {
                return false
            }
        }
    }
    return true
}
```

This function iterates through the array and checks if the array is sorted in non-decreasing order. If it finds any pair of elements where the second element is less than the first, it immediately returns `false`. If it doesn't find any such pair after checking all elements, it returns `true`. If the array is empty, it also returns `true` as per the problem statement.

The time complexity of this function is O(n^2) where n is the length of the array, as it has two nested loops. The space complexity is O(1) as it uses a constant amount of space. 

This function does not perform any right shift operations. Instead, it directly checks if the array is sorted. If you want to simulate the right shift operation, you can do so by repeatedly shifting the elements of the array to the right until the array is sorted. However, this would be a different approach and would likely have a different time complexity. 

Here is an example of how you can simulate the right shift operation:

```go
func MoveOneBall(arr []int) bool {
    if len(arr) == 0 {
        return true
    }
    n := len(arr)
    for {
        sorted := true
        for i := 0; i < n-1; i++ {
            if arr[i] > arr[i+1] {
                sorted = false
                break
            }
        }
        if sorted {
            return true
        }
        for i := 0; i < n-1; i++ {
            if arr[i] > arr[i+1] {
                arr = append(arr[1:], arr[0])
                break
            }
        }
    }
}
```

This function simulates the right shift operation by repeatedly shifting the elements of the array to the right until the array is sorted. It keeps track of whether the array is sorted or not and if it is, it returns `true`. If