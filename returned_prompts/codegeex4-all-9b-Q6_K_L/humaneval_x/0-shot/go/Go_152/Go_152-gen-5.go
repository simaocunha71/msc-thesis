```go
func Compare(game,guess []int) []int {
    result := []int{}
    for i := 0; i < len(game); i++ {
        result = append(result, int(math.Abs(float64(game[i]-guess[i]))))
    }
    return result
}
```