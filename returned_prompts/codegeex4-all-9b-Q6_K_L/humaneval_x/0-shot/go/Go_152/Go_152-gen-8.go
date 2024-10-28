```go
func Compare(game, guess []int) []int {
    res := make([]int, len(game))
    for i, g := range guess {
        res[i] = int(math.Abs(float64(g - game[i])))
    }
    return res
}
```
