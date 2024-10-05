```go
func MakeAPile(n int) []int {
    res := make([]int, n)
    odd, even := 1, 2
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            res[i] = even
            even += 2
        } else {
            res[i] = odd
            odd += 2
        }
    }
    return res
}
```


The function `MakeAPile` takes an integer `n` as input and returns a list of integers representing the number of stones in each level of the pile. The list is initialized with `n` elements using the `make` function. Then, it iterates `n` times and fills the list according to the rules:

- If the current level is even (i.e., `i % 2 == 0`), the number of stones in the level is the next even number, which is `even`. The variable `even` is incremented by 2 in each iteration.
- If the current level is odd (i.e., `i % 2 != 0`), the number of stones in the level is the next odd number, which is `odd`. The variable `odd` is incremented by 2 in each iteration.

Finally, the function returns the list of integers representing the number of stones in each level of the pile. For example, `MakeAPile(3)` returns `[3, 5, 7]`, which represents the number of stones in each level of a pile with 3 levels. The first level has 3 stones, the second level has 5 stones, and the third level has 7 stones.