func MakeAPile(n int) []int {
    var stones []int
    for i := 0; i < n; i++ {
        if i%2 == 0 {
            stones = append(stones, n)
        } else {
            stones = append(stones, n+2)
        }
        n++
    }
    return stones
}