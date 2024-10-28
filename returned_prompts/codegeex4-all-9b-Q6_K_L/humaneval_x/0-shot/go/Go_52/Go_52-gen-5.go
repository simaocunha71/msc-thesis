You can solve this by iterating over the list and checking if each number is less than the threshold. If any number is greater than or equal to the threshold, return false. If you make it through the entire list without returning false, return true.

Here's how you can do it in Go:

```go
func BelowThreshold(l []int, t int) bool {
    for _, num := range l {
        if num >= t {
            return false
        }
    }
    return true
}
```

This function takes a slice of integers `l` and an integer `t` as input, and returns a boolean value. It iterates over the slice `l` using the `range` keyword, which gives you both the index and the value of each element in the slice. If any element is greater than or equal to `t`, it immediately returns false. If it doesn't find any element that's greater than or equal to `t`, it returns true after going through the entire slice.

This is a simple and efficient way to solve the problem, and it works for any slice of integers and any threshold.