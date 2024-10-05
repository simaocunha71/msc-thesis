Here's how you might do it in Go:

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

This function iterates through the first half of the array and compares each element to its corresponding element in the second half. If the elements are not equal, it increments the count. Finally, it returns the count, which represents the minimum number of changes needed to make the array palindromic.