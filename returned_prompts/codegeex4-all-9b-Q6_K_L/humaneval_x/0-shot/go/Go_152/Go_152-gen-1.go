```go
func Compare(game, guess []int) []int {
    var result []int
    for i := 0; i < len(game); i++ {
        result = append(result, int(math.Abs(float64(game[i]-guess[i]))))
    }
    return result
}
```

The solution is straightforward. We iterate through the arrays `game` and `guess` at the same time and calculate the absolute difference between the corresponding elements. We then append this difference to the `result` array, which is returned at the end.