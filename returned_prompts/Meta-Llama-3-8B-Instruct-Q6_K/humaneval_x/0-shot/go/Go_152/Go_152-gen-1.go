```go
package main

import (
    "math"
)

func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, score := range game {
        result[i] = int(math.Abs(float64(score - guess[i])))
    }
    return result
}

func main() {
    game := []int{1, 2, 3, 4, 5, 1}
    guess := []int{1, 2, 3, 4, 2, -2}
    result := Compare(game, guess)
    for _, v := range result {
        println(v)
    }
}
```
In this Go program, we define a function called `Compare` that takes two slices of integers, `game` and `guess`, as input. It returns a new slice of integers, where each element is the absolute difference between the corresponding elements in the `game` and `guess` slices.

In the `main` function, we test the `Compare` function with two example inputs: `game := []int{1, 2, 3, 4, 5, 1}` and `guess := []int{1, 2, 3, 4, 2, -2}`. The output will be the slice `[0, 0, 0, 0, 3, 3]`, which represents the absolute differences between the corresponding elements in the `game` and `guess` slices.

The `math.Abs` function is used to calculate the absolute difference between two numbers. The `range` keyword is used to iterate over the elements of the `game` slice, and the `int` type is used to convert the result of `math.Abs` to an integer. The `make` function is used to create a new slice of integers with the same length as the `game` slice. The `println` function is used to print the elements of the result slice.