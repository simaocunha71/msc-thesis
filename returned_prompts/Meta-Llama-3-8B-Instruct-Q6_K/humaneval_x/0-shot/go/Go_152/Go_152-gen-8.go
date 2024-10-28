Here is a Go solution for the problem:

```go
package main

import (
    "math"
)

func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, v := range game {
        if v == guess[i] {
            result[i] = 0
        } else {
            result[i] = int(math.Abs(float64(guess[i] - v)))
        }
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

This code defines a function `Compare` that takes two slices of integers, `game` and `guess`, as input. It returns a new slice of integers, where each element is the absolute difference between the corresponding elements in `game` and `guess`, unless the elements are equal, in which case the element is 0.

The function uses a loop to iterate over the elements of `game` and `guess`, and for each pair of elements, it calculates the absolute difference and assigns it to the corresponding element in the result slice.

In the `main` function, we test the `Compare` function with the example inputs provided in the problem statement, and print the result. The output should be `[0 0 0 0 3 3]`, which is the expected result.