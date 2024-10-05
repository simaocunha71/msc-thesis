Here is the solution:

```go
func Compare(game,guess []int) []int {
    result := make([]int, len(game))
    for i, v := range game {
        result[i] = int(math.Abs(float64(guess[i] - v)))
    }
    return result
}
```



Explanation:

This function takes two arrays, `game` and `guess`, as input. It creates a new array `result` of the same length as the input arrays. Then it iterates over the input arrays, calculates the absolute difference between the corresponding elements of `guess` and `game`, and stores the result in the `result` array. Finally, it returns the `result` array.

The `math.Abs` function is used to calculate the absolute value of the difference between the guess and the game score. This is because the problem statement asks for the absolute difference between the guess and the score, not the signed difference. The `float64` type is used to convert the integer values to floating-point numbers, which is necessary because `math.Abs` expects a floating-point number as input. The `int` type is used to convert the result back to an integer, which is necessary because the problem statement asks for an integer result.