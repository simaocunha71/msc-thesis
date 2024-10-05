```go
func Compare(game,guess []int) []int {
    var arr []int
    for i := 0; i < len(game); i++ {
        arr = append(arr, int(math.Abs(float64(game[i]-guess[i]))))
    }
    return arr
}
```