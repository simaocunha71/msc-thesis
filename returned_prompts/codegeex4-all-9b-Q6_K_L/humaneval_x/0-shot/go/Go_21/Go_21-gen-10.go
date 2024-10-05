You can create a function to find the minimum and maximum values in the list, then use these values to rescale the list. Here's how you can do it in Go:

```go
func RescaleToUnit(numbers []float64) []float64 {
    minVal := numbers[0]
    maxVal := numbers[0]
    
    // find the min and max in the numbers
    for _, num := range numbers {
        if num < minVal {
            minVal = num
        }
        if num > maxVal {
            maxVal = num
        }
    }
    
    // rescale the numbers
    for i, num := range numbers {
        numbers[i] = (num - minVal) / (maxVal - minVal)
    }
    
    return numbers
}
```

This function first finds the minimum and maximum values in the list of numbers. Then it rescales each number in the list by subtracting the minimum value and dividing by the range (max - min). The result is a new list where the minimum value is 0 and the maximum value is 1.