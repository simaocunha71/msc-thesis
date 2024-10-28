To rescale a list of numbers such that the smallest number becomes 0 and the largest becomes 1, you can use the following steps:

1. Find the minimum and maximum numbers in the list.
2. Subtract the minimum number from all numbers in the list.
3. Divide all numbers in the list by the range (maximum - minimum).

Here is the updated function in Go:

```go
func RescaleToUnit(numbers []float64) []float64 {
    min := numbers[0]
    max := numbers[0]
    
    for _, num := range numbers {
        if num < min {
            min = num
        }
        if num > max {
            max = num
        }
    }
    
    rangeVal := max - min
    
    for i, num := range numbers {
        numbers[i] = (num - min) / rangeVal
    }
    
    return numbers
}
```

This function first finds the minimum and maximum numbers in the list, then subtracts the minimum from each number in the list. Finally, it divides each number by the range (maximum - minimum), resulting in a list where the smallest number is 0 and the largest number is 1.