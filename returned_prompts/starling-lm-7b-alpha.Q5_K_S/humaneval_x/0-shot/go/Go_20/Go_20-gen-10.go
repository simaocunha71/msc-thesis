
```go
package main

import "fmt"

func FindClosestElements(numbers []float64) (res [2]float64) {
    min := float64(1e10)
    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            if abs(numbers[i]-numbers[j]) < min {
                min = abs(numbers[i]-numbers[j])
                res[0] = numbers[i]
                res[1] = numbers[j]
            }
        }
    }
    return
}

func abs(f float64) float64 {
    if f < 0 {
        f = -f
    }
    return f
}

func main() {
    fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))
    fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))
}
```

Explanation:

In this program, we use nested for loops to compare each pair of numbers and select the closest pair.

The `abs` function is used to calculate the absolute value of a number. It is used to compare the absolute value of the difference between the two selected numbers and the current pair of numbers.

In the `main` function, we call the `FindClosestElements` function with a sample array of numbers and print the result.

The `FindClosestElements` function takes an array of numbers as input and returns a slice containing the two closest numbers. It initializes the `min` variable with a large value (`1e10`) to keep track of the minimum difference found so far. It then uses nested for loops to compare each pair of numbers in the array and updates the `min` variable and the result slice if a smaller difference is found. Finally, it returns the result slice.

Overall,