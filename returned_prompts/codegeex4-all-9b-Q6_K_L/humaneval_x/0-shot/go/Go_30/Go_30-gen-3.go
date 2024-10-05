You can use the `filter` function to achieve this. The `filter` function takes a function as an argument, which is used to determine whether an element should be included in the resulting slice. Here's how you can implement the `GetPositive` function using `filter`:

```go
func GetPositive(l []int) []int {
    return filter(func(x int) bool { return x > 0 }, l)
}

func filter(f func(int) bool, l []int) []int {
    res := make([]int, 0)
    for _, x := range l {
        if f(x) {
            res = append(res, x)
        }
    }
    return res
}
```

In this code, `filter` is a helper function that takes a function `f` and a slice `l`, and returns a new slice containing only the elements of `l` that satisfy the condition `f(x)`. The `GetPositive` function then calls `filter` with a function that checks if a number is greater than 0.

Here's how you can use the `GetPositive` function:

```go
func main() {
    l := []int{-1, 2, -4, 5, 6}
    fmt.Println(GetPositive(l)) // Output: [2, 5, 6]

    l = []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
    fmt.Println(GetPositive(l)) // Output: [5, 3, 2, 3, 9, 123, 1]
}
```

This will output:

```
[2 5 6]
[5 3 2 3 9 123 1]
```

Note that the `filter` function can be used with any function that takes an integer and returns a boolean, so it's a very flexible and reusable function.