The solution is to traverse the array from left to right and keep track of the maximum element seen so far. If the current element is greater than or equal to the maximum element seen so far, then the array cannot be arranged in non-decreasing order. Otherwise, update the maximum element seen so far.

Here is the implementation in Go:

```go
func CanArrange(arr []int) int {
    max := arr[0]
    for i := 1; i < len(arr); i++ {
        if arr[i] >= max {
            return -1
        }
        max = arr[i]
    }
    return len(arr) - 1
}
```

The time complexity of this solution is O(n), where n is the length of the array. The space complexity is O(1).