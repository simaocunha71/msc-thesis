Here is the solution in Go:

```go
package main

import (
    "math"
)

func Compare(game []int, guess []int) []int {
    result := make([]int, len(game))
    for i := range game {
        result[i] = int(math.Abs(float64(guess[i] - game[i])))
    }
    return result
}

func main() {
    game := []int{1, 2, 3, 4, 5, 1}
    guess := []int{1, 2, 3, 4, 2, -2}
    result := Compare(game, guess)
    for _, v := range result {
        print(v, " ")
    }
}
```

This program defines a function `Compare` that takes two slices of integers `game` and `guess` and returns a new slice of integers. Each element in the result slice is the absolute difference between the corresponding elements in `game` and `guess`. In other words, it measures how far off each guess was.

In the `main` function, we test the `Compare` function with the example provided in the problem statement. The output of the program is the result of the comparison, which is `[0 0 0 0 3 3]`. This means that the guesses for the first four matches were correct and the guesses for the last two matches were off by 3.