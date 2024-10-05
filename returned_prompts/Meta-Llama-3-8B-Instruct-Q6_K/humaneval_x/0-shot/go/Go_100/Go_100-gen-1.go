The problem can be solved by using a loop to generate the sequence of numbers. Here's a sample implementation in Go:
```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 { // even level
            result[i] = i * 2 + 1
        } else { // odd level
            result[i] = i*2 + 2
        }
    }
    return result
}
```
This function creates a slice of integers with length `n` and then iterates over the slice. For each level, it checks if the level is even or odd using the modulo operator `%`. If the level is even, it sets the number of stones to the next odd number by multiplying `i` by 2 and adding 1. If the level is odd, it sets the number of stones to the next even number by multiplying `i` by 2 and adding 2. Finally, the function returns the slice of numbers.

For example, if you call `MakeAPile(3)`, the function will return the slice `[3, 5, 7]`, which represents the number of stones in each level of the pile. The first level has 3 stones, the second level has 5 stones, and the third level has 7 stones.