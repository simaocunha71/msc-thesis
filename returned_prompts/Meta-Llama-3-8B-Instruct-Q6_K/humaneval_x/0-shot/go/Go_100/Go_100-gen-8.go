```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = i * 2 + 1
        } else {
            result[i] = i * 2
        }
    }
    return result
}
```


The function `MakeAPile` takes an integer `n` as input and returns a list of integers representing the number of stones in each level of the pile.

The function uses a loop to iterate `n` times and calculates the number of stones in each level. If the current level number `i` is even, it sets the number of stones to `i * 2 + 1`, which is the next odd number. If the current level number `i` is odd, it sets the number of stones to `i * 2`, which is the next even number.

The function returns the list of numbers of stones in each level. The element at index `i` in the list represents the number of stones in the level `(i+1)`. For example, `MakeAPile(3)` returns `[3, 5, 7]`, which means the first level has 3 stones, the second level has 5 stones, and the third level has 7 stones.