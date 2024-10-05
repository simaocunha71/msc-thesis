```go
func GetPositive(l []int) []int {
    return filterInts(l, func(i int) bool { return i > 0 })
}

func filterInts(ints []int, f func(int) bool) []int {
    var result []int
    for _, i := range ints {
        if f(i) {
            result = append(result, i)
        }
    }
    return result
}
```
This solution defines a function `GetPositive` that filters a list of integers to return only the positive numbers. It uses a helper function `filterInts` to perform the filtering. The `filterInts` function iterates over the input list, applying the given function `f` to each element. If the function returns `true`, the element is appended to the result list. The `GetPositive` function is then defined in terms of `filterInts`, applying a function that returns `true` for positive integers. The `filterInts` function is a general-purpose filtering function that can be used with different predicates. For example, it could be used to filter a list of strings to return only those that contain a certain substring.