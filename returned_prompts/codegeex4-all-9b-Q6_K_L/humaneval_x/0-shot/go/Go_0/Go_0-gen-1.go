Here is a solution in Go:

```go
func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i] - numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}
```

This function works by iterating over every pair of numbers in the list. If it finds a pair where the absolute difference is less than the threshold, it immediately returns true. If it goes through the entire list without finding such a pair, it returns false.