func XOrY(n, x, y int) int {
    if n <= 1 {
        return y
    }
    for i := 2; i < n; i++ {
        if n % i == 0 {
            return y
        }
    }
    return x
}