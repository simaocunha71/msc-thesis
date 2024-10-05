func MakeAPile(n int) []int {
    var total int
    var result []int
    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            total += i + 1
            result = append(result, total)
        } else {
            total += i + 2
            result = append(result, total)
        }
    }
    return result
}