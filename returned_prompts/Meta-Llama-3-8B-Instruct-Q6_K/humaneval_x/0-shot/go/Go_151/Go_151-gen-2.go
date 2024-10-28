```go
package main

import (
    "math"
)

func DoubleTheDifference(lst []float64) int {
    var sum int
    for _, num := range lst {
        if math.Abs(num) % 2 == 1 && num >= 0 {
            sum += int(math.Pow(num, 2))
        }
    }
    return sum
}

func main() {
    // test cases
    println(DoubleTheDifference([]float64{1, 3, 2, 0})) // 10
    println(DoubleTheDifference([]float64{-1, -2, 0})) // 0
    println(DoubleTheDifference([]float64{9, -2})) // 81
    println(DoubleTheDifference([]float64{0})) // 0
    println(DoubleTheDifference([]float64{})) // 0
}
```



Explanation:

1. The function `DoubleTheDifference` takes a slice of float64 numbers as input.
2. It initializes a variable `sum` to 0, which will be used to store the sum of squares of odd numbers.
3. The function iterates over the input slice using a range loop.
4. For each number in the slice, it checks if the absolute value of the number is odd (using the modulo operator `% 2 == 1`) and if the number is non-negative (using the `>= 0` condition).
5. If both conditions are true, it adds the square of the number to the `sum` variable using the `math.Pow` function to calculate the square.
6. Finally, the function returns the `sum` variable.

In the `main` function, we test the `DoubleTheDifference` function with different input slices and print the results.