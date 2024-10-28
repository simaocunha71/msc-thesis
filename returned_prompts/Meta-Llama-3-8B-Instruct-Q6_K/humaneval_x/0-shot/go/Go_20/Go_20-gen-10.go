```go
package main

import (
    "fmt"
    "math"
)

func FindClosestElements(numbers []float64) [2]float64 {
    var minDiff float64 = math.MaxFloat64
    var closestElements [2]float64

    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[j] - numbers[i])
            if diff < minDiff {
                minDiff = diff
                closestElements[0] = numbers[i]
                closestElements[1] = numbers[j]
            }
        }
    }

    return closestElements
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}
    closestElements := FindClosestElements(numbers)
    fmt.Println(closestElements)
}
```

This Go program defines a function `FindClosestElements` that takes a slice of floating-point numbers as input and returns a slice of two numbers that are closest to each other. It does this by iterating over the input slice and calculating the absolute difference between each pair of numbers. It keeps track of the pair with the smallest difference and returns this pair.

In the `main` function, we test this function with the input `[]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}` and print the result.

The output of this program is:
```
[2 2.2]
```
which are the two numbers in the input slice that are closest to each other.