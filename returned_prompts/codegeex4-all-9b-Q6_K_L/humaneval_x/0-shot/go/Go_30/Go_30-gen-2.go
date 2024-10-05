You can use the built-in function `filter` to achieve this. Here's the solution:

```go
func GetPositive(l []int) []int {
    return filter(l, func(n int) bool {
        return n > 0
    })
}

func filter(l []int, f func(int) bool) []int {
    result := make([]int, 0)
    for _, n := range l {
        if f(n) {
            result = append(result, n)
        }
    }
    return result
}
```

In this code, the `GetPositive` function takes a slice of integers `l` and a function `f` that returns `true` if a number is positive and `false` otherwise. It then calls the `filter` function with `l` and `f` as arguments to get a new slice containing only the positive numbers. The `filter` function iterates over `l`, applies the function `f` to each element, and appends the element to the `result` slice if `f` returns `true`.

You can test the code with the following test cases:

```go
func main() {
    fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6})) // [2, 5, 6]
    fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // [5, 3, 2, 3, 9, 123, 1]
}
```