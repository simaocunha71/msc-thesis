Here is a solution in Go:

```go
func GenerateIntegers(a, b int) []int {
    var result []int
    for i := min(a, b); i <= max(a, b); i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }
    return result
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

This solution first calculates the minimum and maximum of the two numbers. Then it iterates from the minimum to the maximum, checking if each number is even. If it is, it appends it to the result slice. Finally, it returns the result slice.