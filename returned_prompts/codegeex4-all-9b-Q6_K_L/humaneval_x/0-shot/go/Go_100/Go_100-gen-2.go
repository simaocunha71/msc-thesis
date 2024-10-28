func MakeAPile(n int) []int {
    var levels []int
    var stones int
    for i := 1; i <= n; i++ {
        stones += i
        levels = append(levels, stones)
    }
    return levels
}