You can solve this problem using the following steps:

1. Find the maximum and minimum values in the list of numbers.
2. Subtract the minimum value from all the numbers in the list.
3. Divide all the numbers in the list by the difference between the maximum and minimum values.
4. Return the transformed list of numbers.

Here's the implementation of the RescaleToUnit function in Go:

```go
func RescaleToUnit(numbers []float64) []float64 {
    // Find the maximum and minimum values in the list of numbers
    max := numbers[0]
    min := numbers[0]
    for _, num := range numbers {
        if num > max {
            max = num
        }
        if num < min {
            min = num
        }
    }

    // Subtract the minimum value from all the numbers in the list
    for i, num := range numbers {
        numbers[i] = num - min
    }

    // Divide all the numbers in the list by the difference between the maximum and minimum values
    for i, num := range numbers {
        numbers[i] = num / (max - min)
    }

    // Return the transformed list of numbers
    return numbers
}
```

Here's an example of how to use the RescaleToUnit function:

```go
numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0}
transformedNumbers := RescaleToUnit(numbers)
fmt.Println(transformedNumbers) // Output: [0 0.25 0.5 0.75 1]
```