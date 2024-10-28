```go
func BelowThreshold(l []int, t int) bool {
    for _, v := range l {
        if v >= t {
            return false
        }
    }
    return true
}
```
Explanation:

This function iterates over the input list `l` using a `for` loop and a range variable `v`. For each element `v` in the list, it checks if `v` is greater than or equal to the threshold `t`. If it finds an element that is greater than or equal to `t`, it immediately returns `false`, indicating that not all numbers in the list are below the threshold.

If the function completes the iteration without finding any elements greater than or equal to `t`, it returns `true`, indicating that all numbers in the list are below the threshold.

The function uses a simple and efficient algorithm, with a time complexity of O(n), where n is the length of the input list. The space complexity is O(1), as it only uses a constant amount of space to store the threshold and the range variable.