Here's the solution. This function iterates over the list and checks if each number is below the threshold. If it finds a number that is not below the threshold, it returns false. If it finds no such number, it returns true.

```go
func BelowThreshold(l []int, t int) bool {
    for _, n := range l {
        if n >= t {
            return false
        }
    }
    return true
}
```

This function uses the range keyword to iterate over the list. The range keyword returns two values: the index and the value at that index. However, we only care about the value, so we use an underscore to ignore the index. We then use a simple if statement to check if the value is greater than or equal to the threshold. If it is, we return false. If we reach the end of the loop without returning false, we return true.