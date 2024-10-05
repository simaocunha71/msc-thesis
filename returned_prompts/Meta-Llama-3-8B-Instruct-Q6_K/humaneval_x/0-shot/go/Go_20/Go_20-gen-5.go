```go
package main

import (
    "fmt"
    "math"
)

func FindClosestElements(numbers []float64) [2]float64 {
    closestDiff := math.MaxFloat64
    closestPair := [2]float64{}
    for i := 0; i < len(numbers); i++ {
        for j := i + 1; j < len(numbers); j++ {
            diff := math.Abs(numbers[j] - numbers[i])
            if diff < closestDiff {
                closestDiff = diff
                closestPair[0] = numbers[i]
                closestPair[1] = numbers[j]
            }
        }
    }
    return closestPair
}

func main() {
    numbers := []float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}
    fmt.Println(FindClosestElements(numbers)) // Output: [2. 2.2]
}
```
This function FindClosestElements iterates over all pairs of numbers in the input slice and calculates the absolute difference between each pair. It keeps track of the pair with the smallest difference and returns this pair. The main function demonstrates the usage of FindClosestElements with a sample input. The output is as expected. The time complexity of this function is O(n^2), where n is the length of the input slice, because it iterates over all pairs of numbers. This function may not be efficient for large input slices. If efficiency is a concern, a more efficient algorithm may be needed.