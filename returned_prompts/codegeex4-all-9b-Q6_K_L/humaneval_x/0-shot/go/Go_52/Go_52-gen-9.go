You can use the built-in function `all` from the standard library to check if all elements in the slice `l` are below the threshold `t`. Here is the correct code:

```go
func BelowThreshold(l []int, t int) bool {
    return all(func(i int) bool { return i < t }, l)
}

// The all function returns true if the function f returns true for all elements in the slice a.
// >>> all(func(i int) bool { return i < 10 }, []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10})
// true
// >>> all(func(i int) bool { return i < 10 }, []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11})
// false
func all(f func(int) bool, a []int) bool {
    for _, v := range a {
        if !f(v) {
            return false
        }
    }
    return true
}
```

The `all` function iterates over the slice `a` and applies the function `f` to each element. If `f` returns false for any element, the function `all` returns false. If `f` returns true for all elements, the function `all` returns true.