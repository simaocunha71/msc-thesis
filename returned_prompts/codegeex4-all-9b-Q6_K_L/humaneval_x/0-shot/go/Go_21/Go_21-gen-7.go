You can solve this problem by finding the minimum and maximum values in the given list of numbers and then applying a linear transform to each number in the list. Here's how you can implement this in Go:

```go
func RescaleToUnit(numbers []float64) []float64 {
    min := numbers[0]
    max := numbers[0]
    
    // Find the minimum and maximum values in the list
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }
    
    // Apply the linear transform to each number
    for i, num := range numbers {
        numbers[i] = (num - min) / (max - min)
    }
    
    return numbers
}
```

Here's how you can use this function:

```go
func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
    rescaled := RescaleToUnit(numbers)
    fmt.Println(rescaled) // Output: [0 0.25 0.5 0.75 1]
}
```

This function first finds the minimum and maximum values in the given list of numbers. Then, it applies a linear transform to each number in the list, where the minimum value becomes 0 and the maximum value becomes 1. Finally, it returns the transformed list of numbers.