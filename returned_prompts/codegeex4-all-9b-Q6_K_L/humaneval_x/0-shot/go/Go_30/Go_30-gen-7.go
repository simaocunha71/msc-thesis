You can use the filter function to filter out the positive numbers from the list. Here's the modified code:

```go
func GetPositive(l []int) []int {
    return filter(func(x int) bool {
        return x > 0
    }, l)
}

func filter(f func(int) bool, l []int) []int {
    var result []int
    for _, v := range l {
        if f(v) {
            result = append(result, v)
        }
    }
    return result
}
```

The filter function takes a function and a list as arguments, and returns a new list containing only the elements that satisfy the given function. In this case, the function is `func(x int) bool { return x > 0 }`, which returns true if the number is positive.