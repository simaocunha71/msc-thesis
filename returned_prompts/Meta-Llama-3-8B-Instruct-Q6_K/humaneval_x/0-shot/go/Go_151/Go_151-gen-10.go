```go
package main

import (
    "math"
)

func DoubleTheDifference(lst []float64) int {
    sum := 0
    for _, num := range lst {
        if num > 0 && math.Mod(num, 2) == 1 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}

func main() {
    // Test cases
    println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    println(DoubleTheDifference([]float64{-1, -2, 0})) // 0
    println(DoubleTheDifference([]float64{9, -2})) // 81
    println(DoubleTheDifference([]float64{0})) // 0
    println(DoubleTheDifference([]float64{})) // 0
}
```


The code defines a function `DoubleTheDifference` that takes a slice of `float64` numbers as input and returns the sum of squares of the numbers in the list that are odd. It ignores numbers that are negative or not integers. If the input list is empty, it returns 0.

The function uses a for loop to iterate over the input list. For each number, it checks if the number is greater than 0 and if it's odd (using the modulus operator `%` and the `math.Mod` function). If the number is odd, it adds the square of the number to the sum.

In the `main` function, we test the `DoubleTheDifference` function with different input lists and print the results.

Note that the `int` type is used to return the sum, which is an integer. The `float64` type is used for the input numbers, which allows the function to handle floating-point numbers as well. The `math.Pow` function is used to calculate the square of a number. The `math.Mod` function is used to check if a number is odd. The `println` function is used to print the results.