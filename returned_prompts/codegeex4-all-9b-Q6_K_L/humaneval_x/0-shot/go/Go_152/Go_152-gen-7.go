```go
func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, score := range game {
        result[i] = abs(score - guess[i])
    }
    return result
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

The solution is based on the provided code snippet, which correctly calculates the absolute difference between the score and the guess for each match. The `abs` function is a helper function that returns the absolute value of a given integer, which is used in the `Compare` function to calculate the differences. The `Compare` function iterates over the `game` array, calculates the absolute difference between each score and the corresponding guess, and stores the result in the `result` array. Finally, the `result` array is returned as the output of the `Compare` function.