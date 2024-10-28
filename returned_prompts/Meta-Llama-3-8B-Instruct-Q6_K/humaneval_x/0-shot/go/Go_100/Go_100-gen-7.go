```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    if n == 1 {
        result[0] = 1
        return result
    }
    result[0] = n
    for i := 1; i < n; i++ {
        if i % 2 == 0 {
            result[i] = i * 2
        } else {
            result[i] = i * 2 + 1
        }
    }
    return result
}
```


The function `MakeAPile(n int)` returns a list of integers representing the number of stones in each level of the pile. The function initializes an empty list `result` with `n` elements and sets the first element to `n`. It then iterates from `1` to `n-1` and for each iteration, it checks if the current index `i` is even or odd. If `i` is even, it sets the current element in the `result` list to `i * 2`, which is the next even number. If `i` is odd, it sets the current element in the `result` list to `i * 2 + 1`, which is the next odd number. Finally, it returns the `result` list.

For example, if `n` is `3`, the function will return `[3, 5, 7]`, which represents the number of stones in each level of the pile. The first level has `3` stones, the second level has `5` stones, and the third level has `7` stones.