```go
func SumSquares(lst []float64) int {
    sum := 0
    for _, num := range lst {
        num = math.Ceil(num)
        sum += int(num * num)
    }
    return sum
}
```

The function `SumSquares` takes a slice of float64 numbers as input and returns an integer. The function iterates over each number in the slice, rounds it to the nearest integer using `math.Ceil`, and then squares it and adds it to the `sum`. Finally, it returns the total sum.