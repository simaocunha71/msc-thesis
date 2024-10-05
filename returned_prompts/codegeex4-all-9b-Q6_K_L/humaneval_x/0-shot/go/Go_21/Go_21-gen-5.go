You can accomplish this by taking the minimum and maximum values from the list and then subtracting the minimum from all the numbers and dividing by the range. Here's an example of how you can do this in Go:

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
    rangeNum := max - min
    for i, num := range numbers {
        numbers[i] = (num - min) / rangeNum
    }
    return numbers
}
```

In this function, we first find the minimum and maximum values in the list. We then calculate the range of the numbers by subtracting the minimum from the maximum. Finally, we loop through the list again and rescale each number to be between 0 and 1.

Please note that this function modifies the original list. If you don't want to modify the original list, you can create a copy of it before applying the transformation.