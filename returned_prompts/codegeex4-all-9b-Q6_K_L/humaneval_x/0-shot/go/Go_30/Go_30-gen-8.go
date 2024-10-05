You can use the `filter` function to accomplish this. Here's how you can do it:

```go
func GetPositive(l []int) []int {
    return filter(l, func(n int) bool {
        return n > 0
    })
}

func filter(s []int, fn func(int) bool) []int {
    res := []int{}
    for _, i := range s {
        if fn(i) {
            res = append(res, i)
        }
    }
    return res
}
```

The `filter` function takes a slice and a function that returns a boolean value. It iterates over the slice and checks if each element satisfies the function. If it does, it adds it to the result slice.

The `GetPositive` function then uses the `filter` function to return only the positive numbers in the input slice.