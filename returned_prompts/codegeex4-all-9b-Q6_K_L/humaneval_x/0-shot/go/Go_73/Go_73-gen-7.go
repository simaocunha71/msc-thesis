To solve this problem, we need to compare the elements of the array from both ends and count the number of mismatches. For each mismatch, we have two options: change the element at the left end to match the right end, or change the element at the right end to match the left end. We choose the option that requires the fewest changes.

Here is a possible implementation in Go:

```go
func SmallestChange(arr []int) int {
    n := len(arr)
    count := 0
    for i := 0; i < n/2; i++ {
        if arr[i] != arr[n-i-1] {
            count++
        }
    }
    return count
}
```

This implementation has a time complexity of O(n), where n is the length of the array.