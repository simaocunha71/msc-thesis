```go
func DoubleTheDifference(lst []float64) int {
    var sum float64
    for _, num := range lst {
        if num > 0 && num == math.Floor(num) && num%2 != 0 {
            sum += num * num
        }
    }
    return int(sum)
}
```

This function iterates over the list of numbers. If a number is positive, an integer, and odd, it is squared and added to the sum. The sum is then returned as an integer.