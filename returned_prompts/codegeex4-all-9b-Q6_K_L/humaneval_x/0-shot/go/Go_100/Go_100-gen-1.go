```go
func MakeAPile(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        result[i] = 2*(i+1) + n%2
    }
    return result
}
```

I have added a solution in Golang. The function MakeAPile takes an integer n as input and returns a slice of integers representing the number of stones in each level of the pile.

The function first creates a slice of length n to store the result. Then, it uses a for loop to iterate over the levels of the pile. For each level, it calculates the number of stones using the formula 2*(i+1) + n%2, where i is the index of the level. The formula ensures that the number of stones in each level is the next odd or even number depending on whether n is odd or even. Finally, it returns the slice of integers representing the number of stones in each level.