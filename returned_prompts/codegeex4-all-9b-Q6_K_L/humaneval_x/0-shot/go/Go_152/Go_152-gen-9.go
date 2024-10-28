```go
func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i := range game {
        result[i] = int(math.Abs(float64(game[i]) - float64(guess[i])))
    }
    return result
}
```
