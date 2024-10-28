Here is the solution in Go:

```go
package main

import (
    "math"
)

func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, v := range game {
        result[i] = int(math.Abs(float64(guess[i] - v)))
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

This function iterates over the two arrays, calculates the absolute difference between each pair of values, and returns the result as a new array. The `math.Abs` function is used to ensure that the result is always positive, even if the guess was lower than the score. The `main` function is just for testing the `Compare` function. 

When you run this program, it will print the differences between the guesses and the scores for each match. If a guess was correct, the difference will be 0; otherwise, it will be the absolute difference between the guess and the score. 

For example, if you run the program with the example input, it will print `[0, 0, 0, 0, 3, 3]`, which means that the first three guesses were correct and the last two were off by 3. 

Please note that this function does not check if the guesses are valid (i.e., if they are within the range of possible scores). If you need to do that, you will need to add additional code to handle invalid guesses. 

Also, the `Compare` function returns a new array, it does not modify the original arrays. If you want to modify the original arrays, you will need to use a different approach. 