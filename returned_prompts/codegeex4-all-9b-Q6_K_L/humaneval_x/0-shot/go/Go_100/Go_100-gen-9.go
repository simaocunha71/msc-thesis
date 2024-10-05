func MakeAPile(n int) []int {
    var stones []int
    for i := 0; i < n; i++ {
        stones = append(stones, (i+1)*2)
    }
    return stones
}
