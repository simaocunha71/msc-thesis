```go
func RescaleToUnit(numbers []float64) []float64 {
    min := numbers[0]
    max := numbers[0]
    for _, number := range numbers {
        if number < min {
            min = number
        }
        if number > max {
            max = number
        }
    }
    for i, number := range numbers {
        numbers[i] = (number - min) / (max - min)
    }
    return numbers
}
```
