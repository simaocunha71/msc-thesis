func SumToN(n int) int {
    var sum int
    for i := 1; i <= n; i++ {
        sum += i
    }
    return sum
}