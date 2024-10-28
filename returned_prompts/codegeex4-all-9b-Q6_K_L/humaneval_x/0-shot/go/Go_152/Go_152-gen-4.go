```go
func Compare(game, guess []int) []int {
    ans := make([]int, len(game))
    for i, g := range guess {
        ans[i] = int(math.Abs(float64(game[i] - g)))
    }
    return ans
}
```