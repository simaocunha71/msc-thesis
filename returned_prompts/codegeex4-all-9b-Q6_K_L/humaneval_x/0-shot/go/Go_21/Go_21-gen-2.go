```go
func RescaleToUnit(numbers []float64) []float64 {
    min, max := numbers[0], numbers[0]
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }
    for i, num := range numbers {
        numbers[i] = (num - min) / (max - min)
    }
    return numbers
}
```
